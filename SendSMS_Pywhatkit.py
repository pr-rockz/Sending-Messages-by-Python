from email import message
import pywhatkit

phone_number = input("Enter the mobile number: ")

message = input("Enter the text you want to send: ")

pywhatkit.sendwhatmsg(phone_number, message, 21, 53)