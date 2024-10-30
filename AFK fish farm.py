import time

from pynput.mouse import Button, Controller
mouse = Controller()

time.sleep(3)

mouse.press(Button.right)
