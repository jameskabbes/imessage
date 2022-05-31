import user_profile_import
user_profile = user_profile_import.init()
###
#
###
import imessage_support_functions as imsf
import imessage_params as params
import icloud_support_functions as icsf
import iCloud_Contacts
import dir_ops as do #module found in Analytics-Packages
from dir_ops import Path #custom classes found in Analytics-Packages
from dir_ops import Dir #custom classes found in Analytics-Packages
import py_starter as ps

import Message
import PhoneNumber

if __name__ == '__main__':

    # initialize the contacts
    Contacts = iCloud_Contacts.iCloud_Contacts( user_profile = user_profile )

    # Search for a contact or enter a phone number
    print ('Search for a Contact or enter a Phone Number')
    selected_Contacts, input_phone_number = Contacts.get_Contacts_from_input()

    # Get the phone numbers and the corresponding mediums through which to send the message
    PhoneNumbers = []
    mediums = []

    # if the user selected any contacts
    if len(selected_Contacts.Contacts) > 0:

        for Contact in selected_Contacts:

            phone_Option = Contact.get_preffered_Option( 'phones', 'label', ['IPHONE','MOBILE'] )

            if phone_Option.get_attr('label') == 'IPHONE':
                medium = 'iMessage'
            else:
                medium = 'SMS'

            mediums.append( medium )

            new_PhoneNumber = PhoneNumber.PhoneNumber( phone_Option.field )
            PhoneNumbers.append( new_PhoneNumber )


    # see if they input an actual phone number at the end
    new_PhoneNumber = PhoneNumber.PhoneNumber( input_phone_number )
    new_PhoneNumber.print_atts()

    if new_PhoneNumber.valid:
        medium = imsf.get_medium_user()
        mediums.append( medium )
        PhoneNumbers.append( new_PhoneNumber )

    if len(PhoneNumbers) > 0:
        print ('You have selected the following phone numbers and services: ')
        ps.print_for_loop( [ str(PhoneNumbers[i]) + ' : ' + str(mediums[i]) for i in range(len(PhoneNumbers)) ] )
        print()

        # enter the message
        text = input('Enter the message: ')

        # Create the Message inst and send
        Message_inst = Message.Message( text, PhoneNumbers, mediums = mediums )
        Message_inst.send()
