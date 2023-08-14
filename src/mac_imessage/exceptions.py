class NotOnMacOSError(Exception):
    MESSAGE = 'Sending messages on platforms other than macOS is not supported'

class UnsupportedMediumError(Exception):
    MESSAGE = 'Medium {medium} not in supported mediums {supported_mediums}'

class BadPhoneNumberFormatError(Exception):
    MESSAGE = '{phone_number} is not a valid phone number'

