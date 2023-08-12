import kabbes_imessage
import subprocess
import re

def send( message: str, phone_number: str, medium: str, print_off: bool=False ) -> bool:

    """
    message_body: text to be sent in the message
    phone_number: phone number to send the message to
    medium: 'iMessage' or 'SMS'
    """

    if medium.lower() not in kabbes_imessage.MEDIUMS:
        raise kabbes_imessage.exceptions.UnsupportedMediumError('Medium ' + medium + ' not in supported mediums ' + str(list(kabbes_imessage.MEDIUMS.keys())))
    
    selected_medium = kabbes_imessage.MEDIUMS[medium.lower()]
    applescript_code = kabbes_imessage.BASE_APPLESCRIPT.replace("{medium}", selected_medium)
    if not kabbes_imessage.ON_MAC:
        raise kabbes_imessage.exceptions.NotOnMacOSError('This library only functions on MacOS')

    phone_number = _digits_in_phone_number( phone_number )
    if len(phone_number) < 10:
        raise kabbes_imessage.exceptions.BadPhoneNumberFormatError('Formatted Phone Number ' + str(phone_number) + ' is not a valid phone number')

    try:
        result = subprocess.run(['osascript', '-e', applescript_code, phone_number, message], capture_output=True, text=True, check=True)
        if print_off:
            print("Success!")
            print("Output:", result.stdout)
        return True

    except subprocess.CalledProcessError as e:
        if print_off:
            print("Error:", e)
            print("Output:", e.output)

        return False

def send_iMessage( *args ):
    return send( *args, 'iMessage' )

def send_SMS( *args ):
    return send( *args, 'SMS' )

def _digits_in_phone_number( phone_number: str ) -> str:
    return ''.join( re.findall(r'[0-9]*', phone_number) )