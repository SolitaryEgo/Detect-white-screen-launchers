import subprocess
import time
import cv2
import numpy as np
from PIL import ImageGrab


def is_white_screen():
    screenshot = np.array(ImageGrab.grab())
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 255])
    upper_white = np.array([0, 0, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    white_pixels = cv2.countNonZero(mask)
    total_pixels = mask.size
    white_percentage = (white_pixels / total_pixels) * 100
    return white_percentage > 90


first_check = True
while True:
    if is_white_screen():
        if first_check:
            subprocess.run("D:\Microsoft VS Code\Code.exe")
            first_check = False
        else:
            time.sleep(3)
            subprocess.run("D:\Microsoft VS Code\Code.exe")
