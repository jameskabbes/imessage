import mac_imessage

mac_imessage.send(
    message=input('Enter your message: '),
    phone_number=input('Enter the phone number to send: '),
    medium=input(' / '.join(mac_imessage.MEDIUMS) + ': ')
)
