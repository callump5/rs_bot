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

    def start(self):
        print ("Starting Bot")

        if self.image_match('triggers/assets/bag.png', 0.6):
            pag.moveTo(self.coor_x, self.coor_y, self.random_move())
            pag.click()

    def check_inv(self, threshold):

        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')
        template = cv2.imread('triggers/woodcutting/willows/logs.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if len(loc[0]) > 25:
            print ("Bag is full!!")
            self.bank_logs_camelot()
            time.sleep(1)

    def bank_logs_camelot(self):

        self.move_to_trigger('triggers/assets/maps.png', .6)
        self.click_trigger('triggers/assets/maps.png', .6)


        self.move_to_trigger('triggers/woodcutting/yews/yewbank1.png', .8)
        self.click_trigger('triggers/woodcutting/yews/yewbank1.png', .8)

        while True:
            print ('waiting')
            time.sleep(1)
            if self.image_match('triggers/woodcutting/yews/yewbank2.png', .6):
                self.move_to_trigger('triggers/woodcutting/yews/yewbank2.png', .6)
                self.click_trigger('triggers/woodcutting/yews/yewbank2.png', .6)
                time.sleep(8)
                break

        while True:
            print ('waiting')
            if self.image_match('triggers/woodcutting/yews/bankbooth1.png', .875):
                self.move_to_trigger('triggers/woodcutting/yews/bankbooth1.png', .875)

                pag.rightClick()
                time.sleep(2)

                self.move_to_trigger('triggers/woodcutting/yews/bank.png', .8)
                pag.click()

                break

        time.sleep(1)
        self.image_match('triggers/woodcutting/yews/yewlogs.png', .7)
        pag.moveTo(self.coor_x, self.coor_y, self.random_move())
        pag.rightClick()
        self.move_to_trigger('triggers/woodcutting/yews/bankyews.png', .8)
        self.click_trigger('triggers/woodcutting/yews/bankyews.png', .8)
        self.log_count += 1
        print ('Banking Loops: ' +  str(self.log_count))

        while True:
            print ('waiting')
            time.sleep(1)
            if self.image_match('triggers/woodcutting/yews/yewbank1.png', .8):
                self.move_to_trigger('triggers/woodcutting/yews/yewbank1.png', .8)
                self.click_trigger('triggers/woodcutting/yews/yewbank1.png', .8)
                time.sleep(8)
                break


        while True:
            print ('waiting')
            time.sleep(1)
            if self.image_match('triggers/woodcutting/yews/yewspot.png', .8):
                self.move_to_trigger('triggers/woodcutting/yews/yewspot.png', .8)
                self.click_trigger('triggers/woodcutting/yews/yewspot.png', .8)
                time.sleep(8)
                break


        pag.keyDown('up')
        time.sleep(uniform(2, 3))
        pag.keyUp('up')


        def bank_logs(self):

            self.move_to_trigger('triggers/assets/maps.png', .6)
            self.click_trigger('triggers/assets/maps.png', .6)


            self.move_to_trigger('triggers/assets/bank.png', .8)
            self.click_trigger('triggers/assets/bank.png', .8)

            while True:
                print ('waiting')
                time.sleep(1)
                if self.image_match('triggers/assets/banking1.png', .6):
                    self.move_to_trigger('triggers/assets/banking1.png', .6)
                    self.click_trigger('triggers/assets/banking1.png', .6)
                    break

            while True:
                print ('waiting')
                time.sleep(1)
                if self.image_match('triggers/woodcutting/willow/logs.png', .7):
                    self.move_to_trigger('triggers/woodcutting/willow/logs.png', .7)
                    pag.rightClick()
                    self.move_to_trigger('triggers/woodcutting/willow/allwillows.png', .8)
                    self.click_trigger('triggers/woodcutting/willow/allwillows.png', .8)
                    self.log_count += 1
                    print ('Banking Loops: ' +  str(self.log_count))
                    break

            self.move_to_trigger('triggers/assets/spot.png', 0.65)
            self.click_trigger('triggers/assets/spot.png', 0.65)

    def chop_loop(self):
            self.start()
            while True:
                for item in yewimages:
                    print ('checking ' + item['link'])
                    if self.check_inv(0.9):
                        self.bank_logs_camelot()
                    time.sleep(2)
                    if self.image_match(item['link'], item['threshold'] ):
                        self.move_to_trigger(item['link'], item['threshold'])
                        self.click_and_wait('triggers/woodcutting/willows/mytree.png', 0.45)
                        print (str(item['link'] + ' ' + str(item['threshold']) ))

                pag.keyDown('left')
                time.sleep(uniform(1, 2))
                pag.keyUp('left')
                if self.image_match('triggers/woodcutting/yews/chopyew.png', 0.45):
                    self.click_and_wait('triggers/woodcutting/yews/chopyew.png', .45)

bot = ChopBot()

bot.chop_loop()
