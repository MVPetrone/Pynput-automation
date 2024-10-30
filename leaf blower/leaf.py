from pynput.mouse import Button, Controller
mouse = Controller()
import time
import threading

from tkinter import *
root = Tk()

running = False

def up(amount):
    time.sleep(0.1)

    for i in range(amount):
        mouse.move(0,-100)
        time.sleep(0.05)

def down(amount):
    time.sleep(0.1)

    for i in range(amount):
        mouse.move(0,100)
        time.sleep(0.05)

def left(amount):
    time.sleep(0.1)

    for i in range(amount):
        mouse.move(-100,0)
        time.sleep(0.05)

def right(amount):    
    time.sleep(0.1)

    for i in range(amount):                
        mouse.move(100,0)
        time.sleep(0.05)


def loop_8():
    mouse.position = (200,150)
    right(9)
    down(2)
    left(9)
    down(2)
    
    right(9)
    up(2)
    left(9)
    up(2)

def quit_game():
    root.destroy()
    exit()
    quit()
    #threading.Thread(target=start_loop).stop()

def form_ui():
    
    root.bind("<Key>",keyboard)
    
    activate_button = Button(root,text="Activate [F6]",command=lambda:on(True))
    activate_button.grid(row=0,column=0)
        
    deactivate_button = Button(root,text="Deactivate [F7]",command=lambda:on(False))
    deactivate_button.grid(row=1,column=0)

    quit_button = Button(root,text="Quit [F8]",command=lambda:quit_game())
    quit_button.grid(row=2,column=0)

def start_loop():
    global running
    while True:
        
        if running:
            #print("yes")
            #running = False
            loop_8()
            

def on(value):
    global running
    running = value

def keyboard(event):
    key = str(event.keysym)
    if key == "F6":
        on(True)
    elif key == "F7":
        on(False)
    elif key == "F8":
        quit_game()
        
            
form_ui()
threading.Thread(target=start_loop).start()

root.mainloop()

    

