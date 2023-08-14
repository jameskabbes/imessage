import platform
import logging
import warnings

from .utils import *
from . import exceptions

# Setup logger
logging.basicConfig(
    level=logging.INFO,  # Set the desired logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

LOGGER = logging.getLogger(__name__)

# Check user on Mac
ON_MAC = (platform.system() == 'Darwin')
if not ON_MAC:
    warnings.warn(exceptions.NotOnMacOSError.MESSAGE, UserWarning)
    LOGGER.warning(exceptions.NotOnMacOSError.MESSAGE
)

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

