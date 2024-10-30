import time
import pynput

slope1 = True
slope1var = 0

from pynput.mouse import Button, Controller
mouse = Controller()

go = input("Type the level you want to complete: ")

while True:
    if go == "1":
        mouse.position = (976, 186) # Go -------------------
        mouse.click(Button.left,1)

        time.sleep(2.8) #2.8
        mouse.position = (976, 186) # 1 --------------------
        mouse.click(Button.left,1)

        time.sleep(1.5) #1.5
        mouse.position = (976, 186) # 2 --------------------
        mouse.click(Button.left,1)

        time.sleep(1.45)      
        mouse.position = (976, 186) # 3 --------------------
        mouse.click(Button.left,1)

        time.sleep(0.45)      
        mouse.position = (976, 186) # 4 --------------------
        mouse.click(Button.left,1)
        
        time.sleep(0.4)       
        mouse.position = (976, 186) # 5 --------------------
        mouse.click(Button.left,1)

        time.sleep(2.15)       
        mouse.position = (976, 186) # 6 --------------------
        mouse.click(Button.left,1)

        time.sleep(0.7)        
        mouse.position = (976, 186) # 7 --------------------
        mouse.click(Button.left,1)

        time.sleep(0.8)        
        mouse.position = (976, 186) # 8 --------------------
        mouse.click(Button.left,1)

        time.sleep(0.7)        
        mouse.position = (976, 186) # 9 --------------------
        mouse.click(Button.left,1)

        time.sleep(0.7)        
        mouse.position = (976, 186) # 10 -------------------
        mouse.click(Button.left,1)

        time.sleep(0.8)        
        mouse.position = (976, 186) # 11 -------------------
        mouse.click(Button.left,1)

        time.sleep(0.8)        
        mouse.position = (976, 186) # 12 -------------------
        mouse.press(Button.left)
        time.sleep(2)
        mouse.release(Button.left)

        time.sleep(0.6)
        mouse.position = (976, 186) # 13 -------------------
        mouse.press(Button.left)
        time.sleep(1.1)
        mouse.release(Button.left)

        time.sleep(1.3)        
        mouse.position = (976, 186) # 14 -------------------
        mouse.click(Button.left,1)

        time.sleep(0.5)        
        mouse.position = (976, 186) # 15 -------------------
        mouse.click(Button.left,1)

        time.sleep(1)        
        mouse.position = (976, 186) # 16 -------------------
        mouse.click(Button.left,1)

        time.sleep(0.5)        
        mouse.position = (976, 186) # 17 -------------------
        mouse.click(Button.left,1)

        time.sleep(0.8)        
        mouse.position = (976, 186) # 18 -------------------
        mouse.click(Button.left,1)

        time.sleep(0.7)
        mouse.position = (976, 186) # 19 -------------------
        mouse.press(Button.left)
        time.sleep(1.7)
        mouse.release(Button.left)

        time.sleep(5)        
        mouse.position = (976, 186) # 20 -------------------
        mouse.click(Button.left,1)





        time.sleep(1000)



