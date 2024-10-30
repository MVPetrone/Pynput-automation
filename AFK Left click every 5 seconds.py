import time

from pynput.mouse import Controller,Button
mouse = Controller()

time.sleep(2)

while True:
    mouse.click(Button.left,1)
    time.sleep(2)
