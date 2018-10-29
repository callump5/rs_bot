from random import *
import time

import cv2
import numpy as np
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
            pag.moveTo(self.coor_x + 40, self.coor_y + 40, self.random_move())
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

        pag.moveTo(randint(1120, 1130), randint(60, 65), self.random_move())
        pag.click()
        pag.screenshot('triggers/screen.png')
        screen = cv2.imread('triggers/screen.png')


        template = cv2.imread('triggers/bank.png')

        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= .8)

        if len(loc[0]) > 0:
            pag.moveTo(loc[1][0] + 15, loc[0][0] + 15, self.random_move())
            pag.click()
            time.sleep(16)

            pag.screenshot('triggers/screen.png')
            screen = cv2.imread('triggers/screen.png')

            template = cv2.imread('triggers/banking.png')

            res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= .60)

            if len(loc[0]) > 0:

                pag.moveTo(loc[1][0] + 27, loc[0][0] + 22, self.random_move())
                pag.click()
                time.sleep(4)

                pag.screenshot('triggers/screen.png')
                screen = cv2.imread('triggers/screen.png')

                template = cv2.imread('triggers/logs.png')

                res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(res >= .9)

                if len(loc[0]) > 0:
                    self.log_count += len(loc[1])
                    pag.moveTo(loc[1][0] + 15, loc[0][0] +15, self.random_move())
                    pag.rightClick()

                    time.sleep(random())

                    pag.screenshot('triggers/screen.png')
                    screen = cv2.imread('triggers/screen.png')

                    template = cv2.imread('triggers/allwillows.png')

                    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
                    loc = np.where(res >= .8)



                    pag.moveTo(loc[1][0] + 1, loc[0][0] + 1, self.random_move())
                    pag.click()

                    if len(loc[0]) > 0:

                        pag.moveTo(randint(1173, 1175), randint(164, 166), self.random_move())
                        pag.click()
                        print "Logs Chopped: %s" % self.log_count
                        time.sleep(9)

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
                    if self.check_inv(0.85):
                        self.bank_logs()
                    if self.image_match(item['link'], threshitem['thresh-num'] ):
                        self.move_to_trigger(item['link'], threshitem['thresh-num'])
                        self.click_and_wait('triggers/mytree.png', 0.375)
                        print str(item['link'] + ' ' + str(threshitem['thresh-num']) )

            pag.keyDown('left')
            time.sleep(uniform(2, 3))
            pag.keyUp('left')
            if self.image_match('triggers/mytree.png', 0.375):
                self.click_and_wait('triggers/mytree.png', .375)

bot = ChopBot()

bot.chop_loop()
