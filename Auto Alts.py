from PIL import ImageGrab
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time

numb = 1

on = True

time.process_time()
image = ImageGrab.grab()
for y in range(0, 100, 10):
    for x in range(0, 100, 10):
        color = image.getpixel((592, 3))

#advert = 

def run():
    while on == True:
        time.process_time()
        image = ImageGrab.grab()
        for y in range(0, 100, 10):
            for x in range(0, 100, 10):
                color = image.getpixel((592, 3))

        if colour == advert:
            pass
            

def robot():
    mouse.position = (513, 550)
    mouse.click(Button.left,1)

def gene2():
    mouse.position = (594, 636)
    mouse.click(Button.left,1)

def gene1():
    mouse.position = (640, 537)
    mouse.click(Button.left,1)

def cont1():
    mouse.position = (647, 382)
    mouse.click(Button.left,1)

def close():
    time.sleep(0.3)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('w')

def getL1():
    mouse.position = (630, 502)
    mouse.click(Button.left,1)

def cont2():
    mouse.position = (821, 400)
    mouse.click(Button.left,1)

def getL2():
    mouse.position = (647, 644)
    mouse.click(Button.left,1)

def copy():
    mouse.position = (782, 464)
    mouse.click(Button.left,1)

    time.sleep(1)

    with keyboard.pressed(Key.alt):
        
        keyboard.press(Key.tab)
        time.sleep(0.5)
        keyboard.release(Key.tab)
        time.sleep(0.5)                
        if numb == 1:
            keyboard.press(Key.tab)
            time.sleep(0.5)
            keyboard.release(Key.tab)

    time.sleep(1)
        
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

on = True

time.sleep(2)

while on == True:

    gene1()

    time.sleep(2)

    cont1()

    #run() # checks if advert will pop up
    
    #close()

    time.sleep(6)
    
    cont1()

    time.sleep(5)

    getL1()

    time.sleep(9)

    cont2()
    
    time.sleep(9)

    getL2()

    time.sleep(4)

    robot()

    time.sleep(4)

    gene2()

    time.sleep(4)

    copy() # copy link

    time.sleep(3)

    gene2()

    time.sleep(3)

    numb = 0

    

    
