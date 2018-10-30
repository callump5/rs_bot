from random import *
import time

import cv2
import numpy as np
import argparse
import pyautogui as pag

from items import *

pag.FAILSAFE = False

class ChopBot(object):
    def __init__(self):
        self.inventory = []
        self.coor_y = 0
        self.coor_x = 0
        self.log_count = 0

    def random_wait(self, min=.4, max=.6):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return uniform(min, max)

    def random_move(self, min=.7, max=1.5):
        """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
        return uniform(min, max)

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

    def move_to_trigger(self, img, threshold):
        if self.image_match(img, threshold):
            pag.moveTo(self.coor_x + randint(5,10), self.coor_y + randint(4, 7), self.random_move())
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
                else:
                    break

    def start(self):
        print "Starting Bot"

        if self.image_match('triggers/bag.png', 0.6):
            pag.moveTo(self.coor_x, self.coor_y, self.random_move())
            pag.click()

    def check_inv(self, threshold):

        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread('triggers/logs.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if len(loc[0]) > 25:
            print "Bag is full!!"
            self.bank_logs()
            time.sleep(1)

    def bank_logs(self):

        self.move_to_trigger('triggers/maps.png', .6)
        self.click_trigger('triggers/maps.png', .6)


        self.move_to_trigger('triggers/bank.png', .8)
        self.click_trigger('triggers/bank.png', .8)

        while True:
            print 'waiting'
            time.sleep(1)
            if self.image_match('triggers/banking1.png', .6):
                self.move_to_trigger('triggers/banking1.png', .6)
                self.click_trigger('triggers/banking1.png', .6)
                break

        while True:
            print 'waiting'
            time.sleep(1)
            if self.image_match('triggers/logs.png', .7):
                self.move_to_trigger('triggers/logs.png', .7)
                pag.rightClick()
                self.move_to_trigger('triggers/allwillows.png', .8)
                self.click_trigger('triggers/allwillows.png', .8)
                self.log_count += 1
                print 'Banking Loops: ' +  str(self.log_count)
                break

        self.move_to_trigger('triggers/spot.png', 0.65)
        self.click_trigger('triggers/spot.png', 0.65)
    def drop_log(self):
        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread('triggers/log.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 1)
        logs = len(loc[0])

        if len(loc[0]) > 0:
            try:
                pag.moveTo(loc[1][0], loc[0][0], self.random_move())
                pag.mouseDown(button='right')

                pag.screenshot('triggers/screen.png')
                screen = cv2.imread('triggers/screen.png')
                template = cv2.imread('triggers/drop.png')

                res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(res >= 0.6)

                pag.moveTo(loc[1][0], loc[0][0], self.random_move())
                pag.click()
                self.log_count += 1
                print "Logs Chopped: %s" % logs
            except:
                pass

    def chop_loop(self):
            self.start()
            while True:
                for threshitem in thresh:
                    for item in willimages:
                        print 'checking ' + item['link']
                        if self.check_inv(0.9):
                            self.bank_logs()
                        if self.image_match(item['link'], threshitem['thresh-num'] ):
                            self.move_to_trigger(item['link'], threshitem['thresh-num'])
                            self.click_and_wait('triggers/mytree.png', 0.575)
                            print str(item['link'] + ' ' + str(threshitem['thresh-num']) )

                pag.keyDown('left')
                time.sleep(uniform(1, 2))
                pag.keyUp('left')
                if self.image_match('triggers/mytree.png', 0.575):
                    self.click_and_wait('triggers/mytree.png', .575)


bot = ChopBot()

bot.chop_loop()
