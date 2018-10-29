from random import *
import time

import cv2
import numpy as np
import pyautogui as pag

from items import *

pag.FAILSAFE = False

class AttBot(object):
    def __init__(self):
        self.inventory = []
        self.coor_y = []
        self.coor_x = []
        self.log_count = 0

    def start(self):

        print "Starting Bot"
        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread('triggers/bag.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        if len(loc[0]) > 0:
            pag.moveTo(loc[1][0] + 20, loc[0][0] + 20, random())
            pag.click()

    def random_wait(self, min=0.26, max=0.6):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return time.sleep(uniform(min, max))



    def image_match(self, img, threshold):
        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread(img)

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            pag.moveTo(loc[1][0], loc[0][0])
            pag.click()
            time.sleep(randint(17, 25))

    def att_loop(self):
        self.start()
        while True:

            for item in goblin:

                print 'Checking %s' %item['link']
                self.image_match(item['link'], item['thresh'])

            pag.keyDown('left')
            time.sleep(random())
            pag.keyUp('left')

bot = AttBot()
bot.att_loop()