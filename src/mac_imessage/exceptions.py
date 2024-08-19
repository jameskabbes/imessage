import mac_imessage
import typing


class NotOnMacOSError(Exception):
    MESSAGE = 'Sending messages on platforms other than macOS is not supported'


class UnsupportedMediumError(Exception):
    MESSAGE = 'Medium {medium} not in supported mediums {supported_mediums}'

    def __init__(self, medium: typing.Any):
        super().__init__(self.MESSAGE.format(medium=medium,
                                             supported_mediums=str(list(mac_imessage.MEDIUMS))))


class BadPhoneNumberFormatError(Exception):
    MESSAGE = '{phone_number} is not a valid phone number'

    def __init__(self, phone_number: typing.Any):
        super().__init__(self.MESSAGE.format(phone_number=phone_number))
