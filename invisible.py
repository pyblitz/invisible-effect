"""
PyBlitz Invisible Effect 🫥
Real-time invisibility using Python + OpenCV + NumPy

HOW IT WORKS:
1. Capture background (without you in frame)
2. Detect you using color segmentation
3. Replace YOU with the background = INVISIBLE!

RUN: python invisible.py
Press 'q' to quit. Press 'b' to recapture background.
"""
import cv2
import numpy as np
import time

def main():
    print("🫥 PyBlitz Invisible Effect")
    print("Step 1: Move OUT of frame! Capturing background in 3 sec...")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Webcam not found!")
        return
    
    # Capture background
    time.sleep(3)
    background = None
    for _ in range(30):
        ret, background = cap.read()
    background = cv2.flip(background, 1)
    print("✅ Background captured! Come back in frame!")
    print("🔴 Wear something RED for best effect. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        
        # Convert to HSV for color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Red color range (two ranges for red)
        lower1 = np.array([0, 120, 70])
        upper1 = np.array([10, 255, 255])
        lower2 = np.array([170, 120, 70])
        upper2 = np.array([180, 255, 255])
        
        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        mask = mask1 + mask2
        
        # Clean up mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
        
        # Invisibility: replace masked area with background
        mask_inv = cv2.bitwise_not(mask)
        fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
        bg = cv2.bitwise_and(background, background, mask=mask)
        invisible = cv2.addWeighted(fg, 1, bg, 1, 0)
        
        # PyBlitz label
        cv2.putText(invisible, "PyBlitz Invisible! 🫥", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        cv2.imshow("Invisible Effect - PyBlitz (q=quit, b=recapture bg)", invisible)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('b'):
            print("Recapturing background...")
            for _ in range(30):
                ret, background = cap.read()
            background = cv2.flip(background, 1)
    
    cap.release()
    cv2.destroyAllWindows()
    print("👋 Thanks for trying PyBlitz Invisible!")

if __name__ == "__main__":
    main()
