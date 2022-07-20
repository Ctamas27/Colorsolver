from math import sqrt

import keyboard as keyboard
from selenium import webdriver
from PIL import Image
import cv2
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

DRIVER = 'chromedriver'
driver: WebDriver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
driver.get('https://ipon.hu/promo/ipon-fun')
action = ActionChains(driver)

action.move_by_offset(500,500)
action.click()
action.perform()

im2 = Image.open('my_screenshot2.png')
pix2 = im2.load()
green = pix2[470, 790]
purple = pix2[570, 790]
red = pix2[670, 790]
blue = pix2[770, 790]

im3 = Image.open('my_screenshot3.png')
pix3 = im3.load()
yellow = pix3[670, 790]
orange = pix3[770, 790]

colorchain = []
columnOfColor = []

def right():
    action.key_down(Keys.CONTROL).send_keys('ARROW_RIGHT').key_up(Keys.CONTROL).perform()
    barcolors[4] = barcolors[3]
    barcolors[3] = barcolors[2]
    barcolors[2] = barcolors[1]
    barcolors[1] = barcolors[0]
    barcolors[0] = barcolors[4]
    print("right")
    print(barcolors[0], barcolors[1], barcolors[2], barcolors[3])


def left():
    action.key_down(Keys.CONTROL).send_keys('ARROW_LEFT').key_up(Keys.CONTROL).perform()
    barcolors[4] = barcolors[0]
    barcolors[0] = barcolors[1]
    barcolors[1] = barcolors[2]
    barcolors[2] = barcolors[3]
    barcolors[3] = barcolors[4]
    print("left")
    print(barcolors[0], barcolors[1], barcolors[2], barcolors[3])

def fillColorChain(color, column):
    if colorComparator(color, green):
        colorchain.insert(0, "green")
        columnOfColor.append(column)
        time.sleep(0.1)
    if colorComparator(color, purple):
        colorchain.insert(0, "pruple")
        columnOfColor.append(column)
        time.sleep(0.1)
    if colorComparator(color, red):
        colorchain.insert(0, "red")
        columnOfColor.append(column)
        time.sleep(0.1)
    if colorComparator(color, blue):
        colorchain.insert(0, "blue")
        columnOfColor.append(column)
        time.sleep(0.1)
    if colorComparator(color, yellow):
        colorchain.insert(0, "yellow")
        columnOfColor.append(column)
        time.sleep(0.1)
    if colorComparator(color, orange):
        colorchain.insert(0, "orange")
        columnOfColor.append(column)
        time.sleep(0.1)
        

def colorComparator(color1, color2):
    p = distanceCalculator(color1, color2)

    if p < 3 and validColor(color1):
        return True
    else:
        return False
    
def colorCategorizer(color):
    if colorComparator(color, green):
        return "green"
    if colorComparator(color, purple):
        return "purple"
    if colorComparator(color, red):
        return "red"
    if colorComparator(color, blue):
        return "blue"
    if colorComparator(color, yellow):
        return "yellow"
    if colorComparator(color, orange):
        return "orange"
    

def validColor(color1):
    if distanceCalculator(color1, green) < 3 or distanceCalculator(color1, purple) < 3 or distanceCalculator(color1, red) < 3 or distanceCalculator(color1, blue) < 3 or distanceCalculator(color1, yellow) < 3 or distanceCalculator(color1, orange) < 3:
        return True
    else:
        return False

def distanceCalculator(color1, color2):
    r1, g1, b1, a1 = color1
    r2, g2, b2, a2 = color2
    d = sqrt(pow(r2 - r1, 2) + pow(g2 - g1, 2) + pow(b2 - b1, 2))
    p = d / sqrt(255 ^ 2 + 255 ^ 2 + 255 ^ 2)
    p = round(p, 2)
    return p

while True:
    try:
        if keyboard.is_pressed('t'):
            driver.save_screenshot('my_screenshot.png')
            im = Image.open('my_screenshot.png')
            pix = im.load()

            bar1 = pix[470, 790]
            bar2 = pix[570, 790]
            bar3 = pix[670, 790]
            bar4 = pix[770, 790]
            print("Bar colors are loaded")
            break
    except:
        print("Waitin for T key press")


barcolors = ["1", "2", "3", "4", "asd"]

barcolors[0] = colorCategorizer(bar1)
barcolors[1] = colorCategorizer(bar2)
barcolors[2] = colorCategorizer(bar3)
barcolors[3] = colorCategorizer(bar4)

print(barcolors[0], barcolors[1], barcolors[2], barcolors[3])

 #test comment

logicValue = True

counter = 0

while True:
    #time.sleep(0.1)
    im = driver.save_screenshot()
    #screenshot = cv2.imread('my_screenshot.png')
    #im = Image.open('my_screenshot.png')

    pix = im.load()

    screenshot = cv2.circle(screenshot, (470, 790), radius=5, color=(0, 255, 0), thickness=1)
    screenshot = cv2.circle(screenshot, (570, 790), radius=5, color=(0, 255, 0), thickness=1)
    screenshot = cv2.circle(screenshot, (670, 790), radius=5, color=(0, 255, 0), thickness=1)
    screenshot = cv2.circle(screenshot, (770, 790), radius=5, color=(0, 255, 0), thickness=1)

    screenshot = cv2.circle(screenshot, (470, 310), radius=5, color=(0, 0, 255), thickness=1)
    screenshot = cv2.circle(screenshot, (570, 310), radius=5, color=(0, 0, 255), thickness=1)
    screenshot = cv2.circle(screenshot, (670, 310), radius=5, color=(0, 0, 255), thickness=1)
    screenshot = cv2.circle(screenshot, (770, 310), radius=5, color=(0, 0, 255), thickness=1)

    #cv2.imshow('Output', screenshot)
    #cv2.waitKey(1)

    fall1 = pix[470, 310]
    fall2 = pix[570, 310]
    fall3 = pix[670, 310]
    fall4 = pix[770, 310]

    fillColorChain(fall1, "1")
    fillColorChain(fall2, "2")
    fillColorChain(fall3, "3")
    fillColorChain(fall4, "4")

    if logicValue and colorchain:
        print(colorchain[counter], columnOfColor[counter])
        if colorchain[counter] == barcolors[0]:
            if columnOfColor[counter] == "1":
                print("do nothing")
            if columnOfColor[counter] == "2":
                right()
                print("case1")
            if columnOfColor[counter] == "3":
                right()
                time.sleep(0.1)
                right()
                print("case2")
            if columnOfColor[counter] == "4":
                left()
                print("case3")
        if colorchain[counter] == barcolors[1]:
            if columnOfColor[counter] == "1":
                left()
                print("case4")
            if columnOfColor[counter] == "2":
                print("do nothing")
            if columnOfColor[counter] == "3":
                right()
                print("case5")
            if columnOfColor[counter] == "4":
                right()
                time.sleep(0.1)
                right()
                print("case6")
        if colorchain[counter] == barcolors[2]:
            if columnOfColor[counter] == "1":
                left()
                time.sleep(0.1)
                left()
                print("case7")
            if columnOfColor[counter] == "2":
                left()
                print("case8")
            if columnOfColor[counter] == "3":
                print("do nothing")
            if columnOfColor[counter] == "4":
                right()
                print("case9")
        if colorchain[counter] == barcolors[3]:
            if columnOfColor[counter] == "1":
                right()
                print("case10")
            if columnOfColor[counter] == "2":
                left()
                time.sleep(0.1)
                left()
                print("case11")
            if columnOfColor[counter] == "3":
                left()
                print("case12")
            if columnOfColor[counter] == "4":
                print("do nothing")

        logicValue = False
        counter = counter + 1

    if keyboard.is_pressed('y'):
        logicValue = True

    if keyboard.is_pressed('q'):
        break

for i in colorchain:
    print(i)
