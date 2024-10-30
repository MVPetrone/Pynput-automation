import time

from pynput.keyboard import Key, Controller
k = Controller()

while True:
    time.sleep(600)
    k.press(Key.esc)
    
