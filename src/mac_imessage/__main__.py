from mac_imessage import utils

message = input('Enter your message: ')
phone_number = input('Enter the phone number to send: ')
medium = input('SMS / iMessage: ')

utils.send( message, phone_number, medium )

