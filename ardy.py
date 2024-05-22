import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as KeyboardController, Key
import numpy as np
from PIL import ImageGrab

mouse = Controller()
keyboard = KeyboardController()

# colors: [0, 0, 0] = red, [0, 0, 1] = green, [0, 0, 2] = blue

# obstacle fails
x1, y1, x2, y2 = 1031, 183, 1032, 184
x3, y3, x4, y4 = 1287, 209, 1288, 210

# mark of grace
x5, y5, x6, y6 = 677, 413, 678, 414


def failed_obstacle_1():
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    return (screenshot[0, 0, 2]) > 60

def failed_obstacle_3():
    screenshot = np.array(ImageGrab.grab(bbox=(x3, y3, x4, y4)))
    return (screenshot[0, 0, 2]) > 75

# [140 117 9] = grace, [89 75 53] not grace
def mark_of_grace():
    screenshot = np.array(ImageGrab.grab(bbox=(x5, y5, x6, y6)))
    return (screenshot[0, 0, 0]) > 120 and (screenshot[0, 0, 1]) > 100

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

# before running the program:
# 1) make sure your minimap is zoomed in all the way
# 2) climb up to the ardougne rooftop
while True:
    # obstacle 1
    move_mouse_range(634, 184, 647, 226)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(8900, 9250) / 1000)

    if failed_obstacle_1():
        time.sleep(random.randint(2000, 2500) / 1000)
        # click on minimap to run closer to lap start
        move_mouse(1242, 161)
        time.sleep(random.randint(75, 120) / 1000)
        left_click_mouse()
        time.sleep(random.randint(4900, 5250) / 1000)
        
        # climb up
        move_mouse_range(730, 596, 752, 604)
        time.sleep(random.randint(75, 120) / 1000)
        left_click_mouse()
        time.sleep(random.randint(7500, 7850) / 1000)
        continue

    # obstacle 2
    move_mouse_range(545, 413, 561, 416)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(6900, 7250) / 1000)

    # check for mark of grace
    x = random.randint(0, 2)
    if mark_of_grace() and x == 2:
        move_mouse_range(670, 411, 676, 416)
        time.sleep(random.randint(75, 120) / 1000)
        left_click_mouse()
        time.sleep(random.randint(1300, 1350) / 1000)
    
    # obstacle 3
    move_mouse_range(563, 393, 582, 431)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(3100, 3400) / 1000)

    if failed_obstacle_3():
        time.sleep(random.randint(2000, 2500) / 1000)
        # click on minimap to run closer to lap start
        move_mouse(1277, 145)
        time.sleep(random.randint(75, 120) / 1000)
        left_click_mouse()
        time.sleep(random.randint(5200, 5550) / 1000)

        # click on minimap to run even closer to lap start
        move_mouse(1277, 145)
        time.sleep(random.randint(75, 120) / 1000)
        left_click_mouse()
        time.sleep(random.randint(4600, 4950) / 1000)

        # climb up
        move_mouse_range(766, 666, 788, 675)
        time.sleep(random.randint(75, 120) / 1000)
        left_click_mouse()
        time.sleep(random.randint(8000, 8350) / 1000)
        continue

    # obstacle 4
    move_mouse_range(638, 521, 658, 576)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(4500, 4850) / 1000)

    # obstacle 5
    move_mouse_range(726, 647, 750, 676)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(7200, 7550) / 1000)
        
    # obstacle 6
    move_mouse_range(652, 406, 672, 453)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    #time.sleep(random.randint(10800, 11150) / 1000)
    time.sleep(random.randint(11800, 12150) / 1000)

    # climb up
    move_mouse_range(763, 382, 779, 392)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(5900, 6250) / 1000)
