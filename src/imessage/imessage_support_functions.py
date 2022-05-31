import os
import imessage_params as params
import py_starter as ps

def send_message( filtered_phone_number, message_body, script_Path):

    '''run the apple script with the given script path and params'''

    try:
        os.system('osascript {} {} "{}"'.format( script_Path.p, filtered_phone_number, message_body))
    except:
        return False
    return True

def send_imessage( filtered_phone_number, message_body, print_off = True):

    '''send an iMessage with message_body to a given phone_number'''

    if print_off:
        print ('Sending iMessage to ' + str(filtered_phone_number) )
        print (message_body)

    return send_message( filtered_phone_number, message_body, params.send_imessage_script_Path )

def send_sms( filtered_phone_number, message_body, print_off = True ):

    '''send an SMS with message_body to a given phone_number'''

    if print_off:
        print ('Sending SMS to ' + str(filtered_phone_number) )
        print (message_body)

    return send_message( filtered_phone_number, message_body, params.send_sms_script_Path )

def get_medium_user():

    options = ['iMessage','SMS']

    ps.print_for_loop( options )
    ind = ps.get_int_input( 1, len(options), prompt = 'Select the medium for your message: ' ) - 1

    return options[ind]
