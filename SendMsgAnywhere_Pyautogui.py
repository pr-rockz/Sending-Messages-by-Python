import pyautogui
import time

print('\nWelcome to Sending Messages by Python Repository\n')

text = input("Enter the text you want to send: ")

i = 1

number_of_times = int(input("How many times do you want to send the message? "))

time.sleep(3)

while i <= number_of_times:
    pyautogui.typewrite(text)
    pyautogui.press('return')
    i += 1