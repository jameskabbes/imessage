import mac_imessage
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
    if not mac_imessage.ON_MAC:
        mac_imessage.LOGGER.error(mac_imessage.exceptions.NotOnMacOSError.MESSAGE)
        raise mac_imessage.exceptions.NotOnMacOSError(mac_imessage.exceptions.NotOnMacOSError.MESSAGE)

    # Verify the Medium is supported
    if medium.lower() not in mac_imessage.MEDIUMS:
        message = mac_imessage.exceptions.UnsupportedMediumError.MESSAGE.format( medium=medium,supported_mediums=str(list(mac_imessage.MEDIUMS.keys())) )
        mac_imessage.LOGGER.error( message )
        raise mac_imessage.exceptions.UnsupportedMediumError( message )

    selected_medium = mac_imessage.MEDIUMS[medium.lower()]
    applescript_code = mac_imessage.BASE_APPLESCRIPT.replace("{medium}", selected_medium)

    # Verify Phone Number is valid
    phone_number = _get_digits_in_phone_number( phone_number )
    if len(phone_number) < 10:
        error_string = mac_imessage.exceptions.BadPhoneNumberFormatError.MESSAGE.format(phone_number=phone_number)
        mac_imessage.LOGGER.error(error_string)
        raise mac_imessage.exceptions.BadPhoneNumberFormatError(error_string)

    #try to send the message
    try:
        result = subprocess.run(['osascript', '-e', applescript_code, phone_number, message], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        mac_imessage.LOGGER.info( 'unsuccessfully sent ' + medium + ' to ' + phone_number )
        mac_imessage.LOGGER.error('subprocess.CalledProcessError: ' + str(e.output))
        return False

    mac_imessage.LOGGER.info( 'successfully sent ' + medium + ' to ' + phone_number )
    mac_imessage.LOGGER.debug( result )
    return True

def send_iMessage( *args ):
    return send( *args, 'iMessage' )

def send_SMS( *args ):
    return send( *args, 'SMS' )

def _get_digits_in_phone_number( phone_number: str ) -> str:

    """given a string, find all digits in the string and return them"""
    return ''.join( re.findall(r'[0-9]*', phone_number) )