import kabbes_imessage

"""
The most basic usage for this package
"""

def send( message_body: str = '', phone_number: str = '', medium: str = 'iMessage') -> bool:

    """
    message_body: text to be sent in the message
    phone_number: phone number to send the message to
    medium: 'iMessage' or 'SMS'
    """

    message = kabbes_imessage.Message( message_body )
    message.PhoneNumbers.make_PhoneNumber( phone_number, medium = medium )
    return message.send()

def send_iMessage( **kwargs ):

    """Passes to send function adding imessage as medium"""
    send( **kwargs, medium = 'iMessage' )

def send_SMS( **kwargs ):

    """Passes to send function adding SMS as medium"""
    send( **kwargs, medium = 'SMS' )
