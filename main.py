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
    return white_percentage > 90    #计算屏幕中白色元素的百分比的逻辑，如果白色元素的百分比大于90%，则返回True

# 添加一个变量，用于记录是否检测到白屏
first_check = True

while True:
    if is_white_screen():
        if first_check:
            subprocess.run("原神.exe")    #要启动的程序
            first_check = False    #将first_check标志设置为False，之后每次检测到白屏时，先等待3秒再执行操作
        else:
            time.sleep(3)
            subprocess.run("原神.exe")
