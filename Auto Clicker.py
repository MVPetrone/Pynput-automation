from pynput.mouse import Button, Controller
mouse = Controller()

import time
import pynput

clicks = 0
on = True

mouse.click(Button.left,1)
time.sleep(1.5)
mouse.click(Button.left,1)


while on == True:
    
    time.sleep(1.35)
    mouse.click(Button.left,1)

    clicks += 1

    if clicks > 2:
        on = False
    
