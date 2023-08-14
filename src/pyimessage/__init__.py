import platform
import logging
import warnings

# Setup logger
logging.basicConfig(
    level=logging.INFO,  # Set the desired logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger('pyimessage')

# Check user on Mac
ON_MAC = (platform.system() == 'Darwin')
if not ON_MAC:
    message = (
        "This package is designed to work on macOS systems only. Sending messages on other platforms is not supported."
    )
    warnings.warn(message, UserWarning)
    LOGGER.warning(message)

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