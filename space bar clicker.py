import pyautogui 
import keyboard
import time 
keyboard.wait('s')
while not keyboard.is_pressed('b'):
    time.sleep(0.001)         #to control how long between clicks
    pyautogui.press('space')
    #from vid but added time sleep and changed the start nad end lol 