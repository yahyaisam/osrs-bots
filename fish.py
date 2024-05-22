# ---- automated karambwan fishing ----
# client size: 1300 x 800

import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as KeyboardController, Key
import pyautogui
import numpy as np
from PIL import ImageGrab

mouse = Controller()
keyboard = KeyboardController()

# last inv slot empty, rgb: 62 53 41 (green: 53)
# last inv slot has a karambwan, rgb: 65, 97, 46 (green: 97)

# coordinates of the pixel in the last inventory slot
x1, y1, x2, y2 = 1254, 732, 1255, 733
x3, y3, x4, y4 = 69, 718, 70, 719

def inv_is_full():
    # take a screenshot of the last inventory slot
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    # row, column, channel (rgb): red: 0, green: 1, blue: 2
    return (screenshot[0, 0, 1]) > 70 # if green channel > 70 then we have a karambwan (full inv)

def level_up():
    # take a screenshot of the black pixels of the fishing icon upon level up
    screenshot = np.array(ImageGrab.grab(bbox=(x3, y3, x4, y4)))
    return (screenshot[0, 0, 0]) < 5 and (screenshot[0, 0, 2]) < 5 # if red and blue pixels are 0 then we have a lvl up

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

# change the compass from north to south
def change_compass_south():
    # right click compass
    move_mouse_range(1126, 35, 1143, 53)
    time.sleep(random.randint(75, 120) / 1000)
    right_click_mouse()

    # look south
    x, y = pyautogui.position()
    move_mouse_range(1126, y+50, 1143, y+55)
    time.sleep(random.randint(320, 365) / 1000)
    left_click_mouse()

    # lift camera
    keyboard.press(Key.up)
    time.sleep(random.randint(1250, 1450) / 1000)
    keyboard.release(Key.up)

# use the fairy ring after banking
def use_fairy_ring_from_bank():
    # look north
    move_mouse_range(1126, 35, 1143, 53)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # lift camera
    keyboard.press(Key.up)
    time.sleep(random.randint(1250, 1450) / 1000)
    keyboard.release(Key.up)

    # right click fairy ring
    move_mouse_range(51, 155, 78, 169)
    time.sleep(random.randint(75, 120) / 1000)
    right_click_mouse()
    time.sleep(random.randint(75, 120) / 1000)

    # click configure
    x, y = pyautogui.position() # get the y value for the use of an insane algorithm
    move_mouse_range(51, y+50, 78, y+55) # insane algorithm: a range between y+50 and y+55
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # select karamja
    time.sleep(random.randint(10000, 10500) / 1000)
    move_mouse_range(1171, 535, 1230, 549)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # confirm
    time.sleep(random.randint(320, 365) / 1000)
    move_mouse_range(479, 431, 604, 450)
    time.sleep(random.randint(700, 900) / 1000)
    left_click_mouse()

    print("Successfully used the fairy ring from the bank (step 1/5)")

def fish_karambwan():
    change_compass_south()

    # click fishing spot
    move_mouse_range(668, 618, 678, 628)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    print("Successfully clicked the fishing spot (step 2/5)")

    # check a pixel in the last inventory slot for a karambwan every 5 seconds
    t0 = time.time()
    while (not inv_is_full()):
        time.sleep(5000 / 1000)

        # continue fishing if we have stopped due to leveled up
        if (level_up()):
            time.sleep(random.randint(600, 900) / 1000)
            move_mouse_range(647, 433, 657, 441)
            time.sleep(random.randint(75, 120) / 1000)
            left_click_mouse()
        
        # exit the program if it has been longer than 5 minutes and the inventory is not full (has not fished)
        if (time.time() - t0) > 300:
            print("We have problem. Big problem.")
            exit()

# bank after full inventory
def use_fairy_ring_from_karamja():
    # right click fairy ring
    move_mouse_range(612, 235, 646, 254)
    time.sleep(random.randint(75, 120) / 1000)
    right_click_mouse()

    # click configure
    x, y = pyautogui.position()
    move_mouse_range(612, y+50, 646, y+55)
    time.sleep(random.randint(320, 365) / 1000)
    left_click_mouse()

    # select chasm of fire
    time.sleep(random.randint(3000, 3500) / 1000)
    move_mouse_range(1168, 577, 1244, 593)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # confirm
    time.sleep(random.randint(700, 900) / 1000)
    move_mouse_range(479, 431, 604, 450)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    print("Successfully used the fairy ring from Karamja (step 3/5)")

# run to and open bank
def bank():
    move_mouse_range(156, 203, 164, 219)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(10000, 10500) / 1000)

    # bank karambwans
    move_mouse_range(1248, 722, 1264, 736)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(700, 900) / 1000)
    print("Successfully banked the karambwans (step 4/5)")

    # close bank
    keyboard.press(Key.esc)
    time.sleep(random.randint(75, 120) / 1000)
    keyboard.release(Key.esc)
    time.sleep(random.randint(500, 600) / 1000)
    print("Successfully closed the bank (step 5/5)")
    print()

# run the program in a loop
while True:
    use_fairy_ring_from_bank()
    time.sleep(random.randint(5000, 5500) / 1000)

    fish_karambwan()

    use_fairy_ring_from_karamja()
    time.sleep(random.randint(5000, 5500) / 1000)
    bank()
