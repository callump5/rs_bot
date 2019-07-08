from random import *
import time

import cv2
import numpy as np
import argparse
import pyautogui as pag

from items import yewimages, thresh

pag.FAILSAFE = False

class ChopBot(object):
    def __init__(self):
        self.inventory = []
        self.coor_y = 0
        self.coor_x = 0
        self.log_count = 0

        self.triggers = []


    def populate_triggers(self, dict):
        for items in dict:
            my_dict = {
                "trigger": [items['link'], items['threshold']]
            }
            self.triggers.append(my_dict)
        print self.triggers[0]['trigger'][0]

    def image_match(self, img, threshold):
        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread(img)

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            self.coor_x = loc[1][0]
            self.coor_y = loc[0][0]
            return self.coor_x, self.coor_y
        return False

    def threshold_find(self):
        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread(self.triggers[0]['trigger'][0])

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= self.triggers[0]['trigger'][1])
        if len(loc[0]) > 0:
            print 'yes'
            print self.triggers
                self.coor_x = loc[1][0]
                self.coor_y = loc[0][0]
                return self.coor_x, self.coor_y
            else:
                print 'no'
                self.triggers[0]['trigger'][1] -= 0.01
                print self.triggers[0]['trigger'][1]
                return False

    def random_wait(self, min=.4, max=.6):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return uniform(min, max)

    def random_move(self, min=.7, max=1.5):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return uniform(min, max)


    def move_to_trigger(self, img, threshold):
        if self.image_match():
            pag.moveTo(self.coor_x + randint(7,12), self.coor_y + randint(7, 12), self.random_move())
        return False

    def click_trigger(self, img, threshold):
        if self.image_match(img, threshold):
            pag.click()
        return False

    def click_and_wait(self, img, threshold):
        if self.image_match(img,threshold):
            pag.click()

            while True:
                if self.image_match(img, threshold):
                    while self.image_match(img, threshold):
                        time.sleep(1)
                elif self.check_inv(0.9):
                        break
                else:
                break


def chop_loop(self):
    self.start()
    while True:
        for item in yewimages:
            print ('checking ' + item['link'])
            if self.check_inv(0.9):
                self.bank_logs_camelot()
            time.sleep(2)
            if self.fd:
                self.move_to_trigger(item['link'], item['threshold'])
                self.click_and_wait('triggers/woodcutting/yews/chopyew.png', 0.45)
                print (str(item['link'] + ' ' + str(item['threshold'])))

        pag.keyDown('left')
        time.sleep(uniform(1, 2))
        pag.keyUp('left')
        if self.image_match('triggers/woodcutting/yews/chopyew.png', 0.45):
            self.click_and_wait('triggers/woodcutting/yews/chopyew.png', .45)


bot = ChopBot()

bot.populate_triggers(yewimages)
while bot.image_match() == False:
    bot.image_match()