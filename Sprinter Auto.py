import time
from pynput.keyboard import Key, Controller
kb = Controller()

def left():
    kb.press(Key.left)
    kb.release(Key.left)
def right():
    kb.press(Key.right)
    kb.release(Key.right)

def run():
    time.sleep(2)
    while True:
        left()
        
        right()
        

run()


