# 🫥 PyBlitz Invisible Effect

Become invisible using Python + OpenCV! Real-time invisibility effect.

## How It Works
1. Captures your background (without you)
2. Detects red-colored clothing using HSV color segmentation
3. Replaces YOU with the background = **INVISIBLE!**

## Run It
```bash
pip install opencv-python numpy
python invisible.py
```

## Steps
1. Move OUT of frame (3 sec background capture)
2. Come back wearing something **RED** 🔴
3. Watch yourself disappear! 🫥
4. Press `q` to quit, `b` to recapture background

## Requirements
- Python 3.7+
- Webcam
- opencv-python, numpy

Made with 💛 by PyBlitz
