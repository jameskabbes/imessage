import platform

ON_MAC = (platform.system() == 'Darwin')
if not ON_MAC:
    print ('kabbes_imessage Note: no messages will be able to send. You are not running this on a Macintosh system')

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