from random import randint
import pyautogui as pug
import cv2
import numpy as np


def img_match(item):
    # Image of screen
    pug.screenshot('triggers/screen.png')
    template = cv2.imread('triggers/screen.png')

    img = cv2.imread(item)

    # Image match
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7

    # Location
    loc = np.where(res >= threshold)
    if len(loc[0]) > 0:
        return True

    return False