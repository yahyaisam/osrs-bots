# coord for zooming in: 1171, 605 (do this manually before starting the bot)

import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as KeyboardController, Key
import pyautogui
import numpy as np
from PIL import ImageGrab

mouse = Controller()
keyboard = KeyboardController()




def failed_obstacle():
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    return (screenshot[0, 0, 2]) < 40

def left_click_mouse():
    mouse.press(Button.left)
    time.sleep(random.randint(8, 13) / 1000)
    mouse.release(Button.left)

def right_click_mouse():
    mouse.press(Button.right)
    time.sleep(random.randint(8, 13) / 1000)
    mouse.release(Button.right)

def move_mouse_range(x1, y1, x2, y2):
    mouse.position = (random.randint(x1, x2), random.randint(y1, y2))

# for fetching coordinate: reading one pixel
def move_mouse(x1, y1):
    mouse.position = (x1, y1)

# for moving mouse
def action(x1, y1, x2, y2, sleep1, sleep2):
    move_mouse_range(x1, y1, x2, y2)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(sleep1, sleep2) / 1000)


x1, y1, x2, y2 = 1254, 658, 1255, 659
def inv_is_full():
    # take a screenshot of the last inventory slot
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    # row, column, channel (rgb): red: 0, green: 1, blue: 2
    return (screenshot[0, 0, 0]) > 70 # if red channel > 70 then inv is full

x3, y3, x4, y4 = 876, 405, 877, 406
def waterskin_low():
    # take a screenshot of the last inventory slot
    screenshot = np.array(ImageGrab.grab(bbox=(x3, y3, x4, y4)))
    # row, column, channel (rgb): red: 0, green: 1, blue: 2
    return (screenshot[0, 0, 0]) == 255 and (screenshot[0, 0, 1]) == 0 and (screenshot[0, 0, 2]) == 0



#move_mouse_range(82, 389, 83, 390)
# move_mouse(1195, 603)
move_mouse(1171, 605)

restart = True
while True:
    if restart:
        # from grinder to furthest rock north
        action(957, 307, 961, 312, 6500, 6800)
        restart = False

    # from furthest north to middle rock
    action(610, 428, 625, 445, 2750, 3100)
    if inv_is_full():
        # deposit
        action(51, 561, 66, 597, 7000, 7500)
        restart = True
        
        # check if we need to cast humidify
        if waterskin_low():
            # click on spellbook
            move_mouse_range(1069, 767, 1088, 784)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()
            time.sleep(random.randint(300, 600) / 1000)

            # click and cast humidify
            move_mouse_range(1187, 526, 1196, 536)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()
            time.sleep(random.randint(5000, 6000) / 1000)

            # click invent
            move_mouse_range(972, 764, 990, 785)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()

        continue

    # from middle rock to southeast
    action(676, 439, 689, 453, 2750, 3100)
    if inv_is_full():
        # deposit
        action(51, 561, 66, 597, 7000, 7500)
        restart = True

        # check if we need to cast humidify
        if waterskin_low():
            # click on spellbook
            move_mouse_range(1069, 767, 1088, 784)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()
            time.sleep(random.randint(300, 600) / 1000)

            # click and cast humidify
            move_mouse_range(1187, 526, 1196, 536)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()
            time.sleep(random.randint(5000, 6000) / 1000)

            # click invent
            move_mouse_range(972, 764, 990, 785)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()

        continue

    # back to northern rock
    action(583, 377, 597, 392, 2750, 3100)
    if inv_is_full():
        # deposit
        action(51, 561, 66, 597, 7000, 7500)
        restart = True

        # check if we need to cast humidify
        if waterskin_low():
            # click on spellbook
            move_mouse_range(1069, 767, 1088, 784)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()
            time.sleep(random.randint(300, 600) / 1000)

            # click and cast humidify
            move_mouse_range(1187, 526, 1196, 536)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()
            time.sleep(random.randint(5000, 6000) / 1000)

            # click invent
            move_mouse_range(972, 764, 990, 785)
            time.sleep(random.randint(300, 600) / 1000)
            left_click_mouse()

        continue
