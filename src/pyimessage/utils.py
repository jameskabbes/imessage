import pyimessage
import subprocess
import re

def send( message: str, phone_number: str, medium: str, print_off: bool=False ) -> bool:

    """
    message_body: text to be sent in the message
    phone_number: phone number to send the message to
    medium: 'iMessage' or 'SMS'
    print_off: whether to print off the 
    """

    if medium.lower() not in pyimessage.MEDIUMS:
        raise pyimessage.exceptions.UnsupportedMediumError('Medium ' + medium + ' not in supported mediums ' + str(list(pyimessage.MEDIUMS.keys())))
    
    selected_medium = pyimessage.MEDIUMS[medium.lower()]
    applescript_code = pyimessage.BASE_APPLESCRIPT.replace("{medium}", selected_medium)
    if not pyimessage.ON_MAC:
        raise pyimessage.exceptions.NotOnMacOSError('This library only functions on MacOS')

    phone_number = _get_digits_in_phone_number( phone_number )
    if len(phone_number) < 10:
        raise pyimessage.exceptions.BadPhoneNumberFormatError('Formatted Phone Number ' + str(phone_number) + ' is not a valid phone number')

    return _send( applescript_code, message, phone_number, print_off=print_off )

def _send( applescript_code: str, message: str, phone_number: str, print_off: bool=False ):

    """The core functionality to call the Applescript subprocess"""

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

def _get_digits_in_phone_number( phone_number: str ) -> str:

    """given a string, find all digits in the string and return them"""

    return ''.join( re.findall(r'[0-9]*', phone_number) )