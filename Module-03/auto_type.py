import pyautogui
from time import sleep
sleep(5)
for i in range(0, 3):
    pyautogui.write('Hello world ! Right now, I learn python ', interval=0.25)
    pyautogui.press('enter')

