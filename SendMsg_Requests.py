import requests
import time
import schedule

print('\nWelcome to Sending Messages by Python Repository\n')

mobile_number = int(input("Enter the mobile number: "))

message = input("Enter the text you want to send: ")

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': message,    # Replace <your message> with your message
        'key' : 'textbelt'
        })
    
    print(resp.json())
    
schedule.every().day.at('06:00').do(send_message)  # Replace 06:00 with the time you want to send the message

schedule.run_pending()