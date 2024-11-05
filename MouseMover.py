import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x,y,0.5)
    time.sleep(4)
    #used a vid but am const modifying myself