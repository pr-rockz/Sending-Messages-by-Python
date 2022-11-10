import pyautogui
import webbrowser as wb
import time

i = 1

wb.open("web.whatsapp.com")

time.sleep(25)

number_of_messages = int(input("Enter the number of messages you want to send: "))

messages = input("Enter the message you want to send: ")

for i in range(5):
    pyautogui.press(messages)
    pyautogui.press('return')