import pyautogui 
import keyboard
import time 
keyboard.wait('r')
while not keyboard.is_pressed('c'):
    time.sleep(0.01)           #to control how long between clicks
    pyautogui.rightClick()
    #made the right click idea lol but still, main idea from vid