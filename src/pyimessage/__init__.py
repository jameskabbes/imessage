import platform

ON_MAC = (platform.system() == 'Darwin')

import warnings
if ON_MAC:
    message = (
        "This package is designed to work on macOS systems only. "
        "Sending iMessages on other platforms is not supported."
    )
    warnings.warn(message, UserWarning)
    
BASE_APPLESCRIPT = """
on run {phone_number, message}
tell application "Messages"
    set targetService to 1st service whose service type = {medium}
    set targetBuddy to buddy phone_number of targetService
    send message to targetBuddy
end tell
end run
"""

MEDIUMS = {
    "sms": "SMS",
    "imessage": "iMessage"
}

from .utils import *
from . import exceptions