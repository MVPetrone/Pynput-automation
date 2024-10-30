import time
from pynput.mouse import Button, Controller
#from pynput.keyboard import Key, Controller

#keyboard = Controller()
mouse = Controller()

on = True

time.sleep(3)

while on == True:

    mouse.click(Button.right,1)

    time.sleep(0.1)
    mouse.move(0,1090)
    time.sleep(0.1)
    mouse.move(0,1090)

    mouse.click(Button.right,1)

    mouse.click(Button.left,1)

    time.sleep(0.1)

    mouse.move(0,-200)
    time.sleep(0.1)
    mouse.move(0,-200)

    time.sleep(0.1)

    mouse.click(Button.right,1)

    mouse.press(Button.left)
    for i in range(28):
        time.sleep(0.1)
        mouse.move(60,0)
    mouse.release(Button.left)


