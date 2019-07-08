from random import *
import time

import argparse
import pyautogui as pag
import numpy as np
import cv2
import matplotlib.pyplot as plt



class ChopBot(object):
    def __init__(self):
        self.inventory = []
        self.coor_y = 0
        self.coor_x = 0
        self.log_count = 0

    def img_match(self, item, thesh):
        # Image of screen
        pag.screenshot('triggers/screen.png')
        template = cv2.imread('triggers/screen.png')

        img = cv2.imread(item)

        # Image match
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9

        # Location
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            return True

        return False

    def move_to_trigger(self, img, thresh):
        if self.img_match(img, thresh):
            pag.moveTo(self.coor_x, self.coor_y, self.random_move())
        return False


    def click_trigger(self, img, thresh):
        if self.img_match(img, thresh):
            pag.click()
        return False

    def random_wait(self, min=.4, max=.6):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return uniform(min, max)


    def random_move(self, min=.7, max=1.5):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return uniform(min, max)

    def bank_logs(self):
        pag.screenshot('triggers/screen1.png')
        screen = cv2.imread('triggers/screen1.png')
        template = cv2.imread('triggers/assets/bank.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.6)
        if len(loc[0]) > 0:
            pag.moveTo(loc[1][0] + randint(7,10), loc[0][0] + randint(7,10))
            pag.click()
            time.sleep(7 + randint(5,7))




            pag.screenshot('triggers/screen1.png')
            screen = cv2.imread('triggers/screen1.png')
            template = cv2.imread('triggers/assets/booth.png')

            res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.5)
            if len(loc[0]) > 0:
                pag.moveTo(loc[1][0] + randint(7, 10), loc[0][0] + randint(7, 10))
                pag.click()
                time.sleep(2)



            pag.screenshot('triggers/screen1.png')
            screen = cv2.imread('triggers/screen1.png')
            template = cv2.imread('triggers/assets/depositall.png')

            res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.8)
            if len(loc[0]) > 0:
                pag.moveTo(loc[1][0] + randint(7, 10), loc[0][0] + randint(7, 10))
                pag.click()
                time.sleep(2)


            pag.screenshot('triggers/screen1.png')
            screen = cv2.imread('triggers/screen1.png')
            template = cv2.imread('triggers/assets/bank.png')

            res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.6)
            if len(loc[0]) > 0:
                pag.moveTo(loc[1][0] - randint(7, 30), loc[0][0] + 40)
                pag.click()
                time.sleep(5)



    def check_inv(self):

        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread('triggers/woodcutting/willows/logs.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.7)

        if len(loc[0]) > 25:
            print ("Bag is full!!")
            self.bank_logs()
            time.sleep(1)



    def wait_to_chop(self):

        self.check_inv()

        pag.screenshot('triggers/screen1.png')
        screen = cv2.imread('triggers/screen1.png')
        template = cv2.imread('triggers/woodcutting/willows/willowcut.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.5)
        if len(loc[0]) > 0:
            time.sleep(1)
            self.wait_to_chop()

    def chop(self):
        pag.screenshot('triggers/screen.png')
        img = cv2.imread('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png', 1)

        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        low_green = np.array([43, 40, 15])
        high_green = np.array([90, 100, 60])

        mask = cv2.inRange(hsv, low_green, high_green)

        res = cv2.bitwise_and(img,img,mask=mask)

        new_img = np.asarray(mask)
        coors = np.argwhere(new_img == 255)


        numWhitePoints = len( coors )
        index = (numWhitePoints/100) * 90

        print coors[0]
        print "Found {0} points".format( numWhitePoints )

        rand = randint(1, 5) - randint(1, 5)
        pag.moveTo(coors[index][1] + rand, coors[index][0] + rand, 0.2)
        pag.click()


bot = ChopBot()

while True:
    bot.check_inv()
    bot.chop()
    bot.wait_to_chop()
