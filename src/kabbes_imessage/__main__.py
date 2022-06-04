import kabbes_imessage

###
message_body = input( 'Enter a message to send (enter to exit): ' )
Message_inst = kabbes_imessage.Message( message_body )

while True:
    phone_number = input( 'Enter a phone number to send this message to (enter to exit): ')
    if phone_number == '':
        break
    
    PhoneNumber_inst = kabbes_imessage.PhoneNumber( long_phone_number=phone_number )  
    if PhoneNumber_inst.valid:
        Message_inst.PhoneNumbers._add_PhoneNumber( PhoneNumber_inst )

Message_inst.send()
