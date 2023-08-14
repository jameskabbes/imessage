import pyimessage
import subprocess
import re

def send( message: str, phone_number: str, medium: str ) -> bool:

    """
    message_body: text to be sent in the message
    phone_number: phone number to send the message to
    medium: 'iMessage' or 'SMS'

    returns: boolean saying where the Applescript was called successfully
    """

    # Verify platform is macOS
    selected_medium = pyimessage.MEDIUMS[medium.lower()]
    applescript_code = pyimessage.BASE_APPLESCRIPT.replace("{medium}", selected_medium)
    if not pyimessage.ON_MAC:
        pyimessage.LOGGER.error(pyimessage.exceptions.NotOnMacOSError.MESSAGE)
        raise pyimessage.exceptions.NotOnMacOSError(pyimessage.exceptions.NotOnMacOSError.MESSAGE)

    # Verify the Medium is supported
    if medium.lower() not in pyimessage.MEDIUMS:
        message = pyimessage.exceptions.UnsupportedMediumError.MESSAGE.format( medium=medium,supported_mediums=str(list(pyimessage.MEDIUMS.keys())) )
        pyimessage.LOGGER.error( message )
        raise pyimessage.exceptions.UnsupportedMediumError( message )

    # Verify Phone Number is valid
    phone_number = _get_digits_in_phone_number( phone_number )
    if len(phone_number) < 10:
        error_string = pyimessage.exceptions.BadPhoneNumberFormatError.MESSAGE.format(phone_number=phone_number)
        pyimessage.LOGGER.error(error_string)
        raise pyimessage.exceptions.BadPhoneNumberFormatError(error_string)

    #try to send the message
    try:
        result = subprocess.run(['osascript', '-e', applescript_code, phone_number, message], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        pyimessage.LOGGER.info( 'unsuccessfully sent ' + medium + ' to ' + phone_number )
        pyimessage.LOGGER.error('subprocess.CalledProcessError: ' + str(e.output))
        return False

    pyimessage.LOGGER.info( 'successfully sent ' + medium + ' to ' + phone_number )
    pyimessage.LOGGER.debug( result )
    return True

def send_iMessage( *args ):
    return send( *args, 'iMessage' )

def send_SMS( *args ):
    return send( *args, 'SMS' )

def _get_digits_in_phone_number( phone_number: str ) -> str:

    """given a string, find all digits in the string and return them"""
    return ''.join( re.findall(r'[0-9]*', phone_number) )