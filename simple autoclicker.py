import pyautogui 
import keyboard
import time 
keyboard.wait('m')
while not keyboard.is_pressed('n'):
    time.sleep(0.001)           #to control how long between clicks
    pyautogui.click()
    #from vid but added time sleep and changed the start and end lol``