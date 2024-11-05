import pyautogui
import time
import keyboard

keyboard.wait("o")
while not keyboard.is_pressed('p'):
    time.sleep(0.001)
    pyautogui.scroll(99999999)
    #made without a vid. Made this all by myself