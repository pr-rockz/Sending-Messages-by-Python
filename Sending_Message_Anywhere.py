import pyautogui
import time

text = "Uth ja Arpitchod"

i = 1

time.sleep(3)

while i <= 20:
    pyautogui.typewrite(text)
    pyautogui.press('return')
    i += 1
'''
spam mat crow
spam mat crow
spam mat crow
spam mat crow
spam mat crow
spam mat crow
spam mat crow
spam mat crow
spam mat crow
'''