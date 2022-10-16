import pyautogui
import webbrowser as wb
import time

i = 1

wb.open("web.whatsapp.com")

time.sleep(25)

for i in range(5):
    pyautogui.press("Your text here")
    pyautogui.press('return')
    pyautogui.press("Your text here")