import time
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as KeyboardController, Key
import pyautogui
import numpy as np
from PIL import ImageGrab

mouse = Controller()
keyboard = KeyboardController()

# coordinates when first climbing up to check if we are on the western or eastern tile
x1, y1, x2, y2 = 86, 310, 87, 311
# rgb for eastern tile: 115, 104, 54
# rgb for western tile: 52, 82, 5
def eastern_tile_1():
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    return (screenshot[0, 0, 0]) == 115 and (screenshot[0, 0, 1]) == 104 and (screenshot[0, 0, 2]) == 54

# east tile rgb of cactus area: 79, 86, 41
# west tile rgb of cactus area: 142, 128, 67

# coordinates for the cactus to determine if we are on the eastern or western tile after the first obstacle
x3, y3, x4, y4 = 340, 360, 341, 361
# east tile rgb of cactus area: 79, 86, 41
# west tile rgb of cactus area: 142, 128, 67
def eastern_tile_2():
    screenshot = np.array(ImageGrab.grab(bbox=(x3, y3, x4, y4)))
    return (screenshot[0, 0, 0]) < 120 # if red value < 130: eastern tile

# used for after climbing up to the 2nd pyramid floor
x5, y5, x6, y6 = 82, 389, 83, 390
# east tile rgb: 115, 104, 54
def eastern_tile_3():
    screenshot = np.array(ImageGrab.grab(bbox=(x5, y5, x6, y6)))
    #return (screenshot[0, 0, 0]) == 115 and (screenshot[0, 0, 1]) == 104 and (screenshot[0, 0, 2]) == 54
    return (screenshot[0, 0, 0]) == 115

x7, y7, x8, y8 = 309, 206, 310, 207
# north rgb: 33, 30, 16
# south rgb: 100, 104, 49
def northern_tile_1():
    screenshot = np.array(ImageGrab.grab(bbox=(x7, y7, x8, y8)))
    return (screenshot[0, 0, 0]) < 100 # if red value < 100: northern tile

x9, y9, x10, y10 = 68, 454, 69, 455
# east: 115, 104, 54
# west: 49, 78, 5
def eastern_tile_4():
    screenshot = np.array(ImageGrab.grab(bbox=(x9, y9, x10, y10)))
    return (screenshot[0, 0, 0]) > 70 # if red value > 70: eastern tile

x11, y11, x12, y12 = 476, 429, 477, 430
def pyramid_block():
    screenshot = np.array(ImageGrab.grab(bbox=(x11, y11, x12, y12)))
    return (screenshot[0, 0, 0]) > 120 and (screenshot[0, 0, 1]) > 100 # red > 120 and green > 100

a, b, c, d = 487, 330, 488, 331
# fully out: 186, 150, 88
def pyramid_block_floor_1_fully_out():
    screenshot = np.array(ImageGrab.grab(bbox=(a, b, c, d)))
    return (screenshot[0, 0, 0]) == 186 and (screenshot[0, 0, 1]) == 150 and (screenshot[0, 0, 2]) == 88

x13, y13, x14, y14 = 891, 393, 892, 394
# east: 76, 49, 27
def eastern_tile_5():
    screenshot = np.array(ImageGrab.grab(bbox=(x13, y13, x14, y14)))
    return (screenshot[0, 0, 0]) == 76 and (screenshot[0, 0, 1]) == 49 and (screenshot[0, 0, 2]) == 27

x15, y15, x16, y16 = 377, 205, 378, 206
# east: 38, 61, 4
def eastern_tile_6():
    screenshot = np.array(ImageGrab.grab(bbox=(x15, y15, x16, y16)))
    return (screenshot[0, 0, 0]) == 38 and (screenshot[0, 0, 1]) == 61 and (screenshot[0, 0, 2]) == 4

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
# def move_mouse(x1, y1):
#     mouse.position = (x1, y1)

# for fetching coordinate: reading one pixel
def move_mouse(coord):
    mouse.position = coord

# action with no sleep at the end
def action(x1, y1, x2, y2):
    move_mouse_range(x1, y1, x2, y2)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

# for moving mouse
def action(x1, y1, x2, y2, sleep1, sleep2):
    move_mouse_range(x1, y1, x2, y2)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()
    time.sleep(random.randint(sleep1, sleep2) / 1000)

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
    time.sleep(random.randint(75, 120) / 1000) # TODO: remove?

def change_compass_north():
    move_mouse_range(1126, 35, 1143, 53)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # lift camera
    keyboard.press(Key.up)
    time.sleep(random.randint(1250, 1450) / 1000)
    keyboard.release(Key.up)
    time.sleep(random.randint(75, 120) / 1000) # TODO: remove?

def change_compass_east():
    # right click compass
    move_mouse_range(1126, 35, 1143, 53)
    time.sleep(random.randint(75, 120) / 1000)
    right_click_mouse()

    # look east
    x, y = pyautogui.position()
    move_mouse_range(1126, y+38, 1143, y+43)
    time.sleep(random.randint(320, 365) / 1000)
    left_click_mouse()

    # lift camera
    keyboard.press(Key.up)
    time.sleep(random.randint(1250, 1450) / 1000)
    keyboard.release(Key.up)
    time.sleep(random.randint(75, 120) / 1000) # TODO: remove?



#######################  TODO
# floor 1 red obstacle 1: east or west (west good, covered)
# ^ uncertainty
# PROBLEM: TODO: reads west at the start of 2nd floor even tho it's east
# one lap: 3 min 40s or so
# TODO: click inv after changing zoom setting
# ^ before starting a new lap
# TODO: humidify (same code as sandstone, before starting new lap)





while True:

    # climb up
    action(696, 289, 723, 332, 2500, 2850)

    # NOTE: compass has to be pointed north
    eastern = False
    # red obstacle 1
    if (eastern_tile_1()):
        eastern = True
        # red obstacle 1
        action(632, 135, 650, 152, 4150, 4500)
        # green obstacle 1
        action(624, 282, 651, 297, 5200, 5550)
        change_compass_south()
        action(397, 433, 422, 465, 7600, 7950)
        # pyramid block + green obstacle 2
    else:
        # red obstacle 1
        action(644, 135, 666, 151, 4150, 4500)
        # green obstacle 1
        action(643, 282, 668, 296, 5200, 5550)
        change_compass_south()
        action(376, 435, 400, 465, 7600, 7950)
        # pyramid block + green obstacle 2

    while not(pyramid_block_floor_1_fully_out()):
        time.sleep(random.randint(1000, 1500) / 1000)
        continue

    action(496, 291, 502, 297, 9300, 9650)
    # red obstacle 1
    action(724, 229, 755, 253, 2500, 2850)
    change_compass_north()
    # green obstacle 2
    action(533, 451, 570, 487, 6350, 6700)
    # green obstacle 3
    action(516, 405, 550, 439, 5400, 5750)
    # climb up to the 2nd floor
    action(566, 358, 603, 392, 2450, 2800)








    # 2nd floor
    eastern = False
    if (eastern_tile_3()):
        print("if: east")
        eastern = True
        action(625, 342, 652, 370, 6600, 6950)
    else:
        print("else: west")
        action(642, 340, 671, 371, 6600, 6950)

    # always the same tile
    action(627, 277, 653, 296, 5300, 5650)
    change_compass_south()
    action(546, 414, 574, 442, 5900, 6250)
    action(465, 233, 489, 250, 3400, 3750)
    action(582, 234, 610, 250, 7800, 8150)
    change_compass_north()
    action(591, 455, 606, 488, 4400, 4750)
    action(519, 414, 551, 444, 4550, 4900)
    # climb up to 3rd floor
    action(530, 361, 555, 395, 3300, 3650)




    # -- 3rd floor
    # obstacle 2
    # east or west?
    eastern = False
    if (eastern_tile_4()):
        eastern = True
        # green obstacle 1
        action(625, 358, 654, 371, 4500, 4850)
        # green obstacle 2
        action(625, 320, 656, 351, 7250, 7600)
    else:
        # green obstacle 1
        action(641, 357, 672, 373, 4500, 4850)
        # green obstacle 2
        action(643, 321, 673, 348, 7250, 7600)

    # always same tile
    change_compass_south()

    # ---moving block (marked tile with the text "here")
    while not(pyramid_block()):
        time.sleep(random.randint(1000, 1500) / 1000)
        continue

    # obstacle 3
    action(389, 296, 411, 318, 8500, 8850)

    # obstacle 4
    action(651, 309, 654, 311, 7500, 7850)

    change_compass_north()

    # climb up to 4th floor
    action(532, 338, 559, 369, 3500, 3850)







#    --- 4th floor
    eastern = False
    if (eastern_tile_5()):
        print("if: east")
        eastern = True
        # green obstacle 1
        action(625, 351, 652, 376, 3900, 4250)
        change_compass_south()
        # green obstacle 2
        action(616, 453, 630, 481, 4150, 4500)
    else:
        print("else: west")
        action(642, 348, 672, 375, 3900, 4250)
        change_compass_south()
        # green obstacle 2
        action(591, 454, 606, 484, 4000, 4350)

    # red obstacle 1 + green obstacle 3
    action(514, 297, 542, 317, 3300, 3650)
    action(618, 347, 649, 372, 3900, 4250)
    change_compass_north()
    action(618, 412, 633, 440, 3050, 3400)
    action(552, 367, 581, 394, 3050, 3400)






    # --- 5th floor (last)
    eastern = False
    change_compass_east()
    if (eastern_tile_6()):
        print("if: east")
        eastern = True
        # climb to pick up pyramid top
        action(647, 385, 659, 398, 5000, 5350)
    else:
        print("else: west")
        # climb to pick up pyramid top
        action(646, 365, 658, 380, 5000, 5350)

    change_compass_south()
    # red + green obstacle
    action(545, 407, 575, 436, 2800, 3150)
    action(617, 370, 648, 398, 3100, 3450)
    change_compass_north()
    # exit through doorway (finish)
    action(617, 399, 625, 408, 1450, 1800)





    # climb rocks to go to Simon
    action(307, 479, 320, 489, 8000, 8350)

    # click on settings
    move_mouse_range(1204, 763, 1219, 785)
    time.sleep(random.randint(400, 750) / 1000)
    left_click_mouse()

    # coords to zoom in (for simon): 1195, 603
    time.sleep(random.randint(75, 120) / 1000)
    move_mouse((1195, 603))
    time.sleep(random.randint(400, 750) / 1000)
    left_click_mouse()

    # click invent
    time.sleep(random.randint(75, 120) / 1000)
    move_mouse_range(971, 764, 991, 785)
    time.sleep(random.randint(400, 750) / 1000)
    left_click_mouse()

    # click on the pyramid top
    time.sleep(random.randint(75, 120) / 1000)
    move_mouse_range(1163, 511, 1180, 524)
    time.sleep(random.randint(400, 750) / 1000)
    left_click_mouse()

    # -------- Simon
    a1, b1, c1, d1 = 8, 28, 1289, 752
    exclude_region = 254, 526, 513, 700 # exclude the tent near Simon, which seems to be interfering with the rgb value of his hat
    target_rgb = (76, 63, 27)  # hat

    wanted_coords = (0, 0)
    prev_coords = (0, 0)

    # TODO: client size: 1300, 800
    counter = 0
    while True:
        # print(counter)
        screenshot = ImageGrab.grab(bbox=(a1, b1, c1, d1))
        found_match = False

        for y in range(b1, d1):
            for x in range(a1, c1):

                if exclude_region[0] <= x < exclude_region[2] and exclude_region[1] <= y < exclude_region[3]:
                    continue
                
                rgb_value = screenshot.getpixel((x - a1, y - b1))

                if rgb_value == target_rgb:
                    found_match = True
                    wanted_coords = (x, y+8)
                    break

            if found_match:
                break

        if found_match and wanted_coords == prev_coords:
            counter += 1
        else:
            counter = 0

        if counter >= 1:
            break

        prev_coords = wanted_coords

        time.sleep(0.0166)

    move_mouse(wanted_coords)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # wait a bit for the camera to stand still before taking a screenshot
    time.sleep(random.randint(2500, 3500) / 1000)

    q, w, e, r = 8, 30, 1082, 750
    target_rgb = (87, 6, 148) # marked purple title
    wanted_coords = (0, 0)
    found_match = False
    screenshot = ImageGrab.grab(bbox=(q, w, e, r))
    for y in range(w, r):
        for x in range(q, e):
            
            rgb_value = screenshot.getpixel((x - q, y - w))

            if rgb_value == target_rgb:
                found_match = True
                wanted_coords = (x, y)
                break

        if found_match:
            break

    move_mouse_range(wanted_coords[0], wanted_coords[1], wanted_coords[0]+2, wanted_coords[1]+2)
    time.sleep(random.randint(75, 120) / 1000)
    left_click_mouse()

    # climb down to get ready for a new lap
    time.sleep(random.randint(3800, 4150) / 1000)
    action(685, 427, 722, 449, 4700, 5050)

    # TODO: find coords to zoom fully out again, before starting a new pyramid lap
    # click on settings
    move_mouse_range(1204, 763, 1219, 785)
    time.sleep(random.randint(400, 750) / 1000)
    left_click_mouse()

    # coords to zoom fully out: 1153, 607
    time.sleep(random.randint(75, 120) / 1000)
    move_mouse((1153, 607))
    time.sleep(random.randint(400, 750) / 1000)
    left_click_mouse()

