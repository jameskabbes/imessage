import mac_imessage
import subprocess
import re
import typing


class SendViaMediumKwargs(typing.TypedDict):
    message: mac_imessage.custom_types.MESSAGE
    phone_number: mac_imessage.custom_types.PHONE_NUMBER


class SendKwargs(SendViaMediumKwargs):
    medium: mac_imessage.custom_types.MEDIUMS


type SendReturn = bool


def send(**kwargs: typing.Unpack[SendKwargs]) -> SendReturn:

    medium = kwargs['medium']
    message = kwargs['message']
    phone_number = kwargs['phone_number']

    # Verify platform is macOS
    if not mac_imessage.ON_MAC:
        mac_imessage.LOGGER.error(
            mac_imessage.exceptions.NotOnMacOSError.MESSAGE)
        raise mac_imessage.exceptions.NotOnMacOSError(
            mac_imessage.exceptions.NotOnMacOSError.MESSAGE)

    # verify medium is supported
    if medium not in mac_imessage.MEDIUMS:
        raise mac_imessage.exceptions.UnsupportedMediumError(medium)

    # Verify Phone Number is valid
    formatted_phone_number = _get_digits_in_phone_number(phone_number)
    if len(formatted_phone_number) < 10:
        raise mac_imessage.exceptions.BadPhoneNumberFormatError(
            phone_number)

    # try to send the message
    try:
        result = subprocess.run(['osascript', '-e', mac_imessage.BASE_APPLESCRIPT.replace('{medium}', medium),
                                formatted_phone_number, message], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        mac_imessage.LOGGER.info(
            'unsuccessfully sent ' + medium + ' to ' + phone_number)
        mac_imessage.LOGGER.error(
            'subprocess.CalledProcessError: ' + str(e.output))
        return False

    mac_imessage.LOGGER.info('successfully sent ' +
                             medium + ' to ' + phone_number)
    mac_imessage.LOGGER.debug(result)
    return True


def send_imessage(**kwargs: typing.Unpack[SendViaMediumKwargs]) -> SendReturn:
    return send(**kwargs, medium='imessage')


def send_sms(**kwargs: typing.Unpack[SendViaMediumKwargs]) -> SendReturn:
    return send(**kwargs, medium='sms')


def _get_digits_in_phone_number(phone_number: mac_imessage.custom_types.PHONE_NUMBER) -> mac_imessage.custom_types.PHONE_NUMBER:
    """given a string, find all digits in the string and return them"""
    return ''.join(re.findall(r'[0-9]*', phone_number))
