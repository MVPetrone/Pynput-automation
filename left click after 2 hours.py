import time
from pynput.mouse import Button, Controller
mouse = Controller()

time.sleep(7200)
mouse.click(Button.left,1)
