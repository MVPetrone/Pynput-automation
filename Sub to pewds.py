import pynput        #To change keyboard and mouse
import time          #To tell the script to wait

from pynput.mouse import Button, Controller             #Change 1
mouse = Controller()

mouse.position = (15, 1014)
mouse.click(Button.left,1)

from pynput.keyboard import Key, Controller             #Change 2
keyboard = Controller()

time.sleep(1.3)      #Wait

keyboard.type('chrome')

time.sleep(1)        #Wait

keyboard.press(Key.enter)

time.sleep(2.5)      #Wait

from pynput.keyboard import Key, Controller             #Change 3
keyboard = Controller()

keyboard.type('https://www.youtube.com/user/PewDiePie')
keyboard.press(Key.enter)

from pynput.mouse import Button, Controller             #Change 4
mouse = Controller()

time.sleep(6)        #Wait

mouse.position = (1054, 390)
mouse.click(Button.left, 1)

time.sleep(1)        #Wait

mouse.position = (1270,10)
mouse.click(Button.left,1)
