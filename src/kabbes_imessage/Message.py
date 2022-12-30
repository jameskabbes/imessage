from parent_class import ParentClass
import kabbes_imessage
import os

class Message( ParentClass ):

    _ONE_LINE_ATTS = ['type','PhoneNumbers']
    _IMP_ATTS = ['message','PhoneNumbers']

    def __init__( self, message, PhoneNumbers_inst = None, phone_numbers = [], **kwargs ):

        ParentClass.__init__( self )

        self.message = message

        # read in phone numbers
        if type(PhoneNumbers_inst) == kabbes_imessage.PhoneNumbers:
            self.PhoneNumbers = PhoneNumbers_inst
        else:
            self.PhoneNumbers = kabbes_imessage.PhoneNumbers()

        # if given phone numbers
        for phone_number in phone_numbers:
            self.PhoneNumbers.make_PhoneNumber( long_phone_number = phone_number )            

    def send( self, print_off: bool = True ):

        success = True

        if kabbes_imessage.ON_MAC:
            for PhoneNumber_inst in self.PhoneNumbers:

                if print_off:
                    print ('Sending ' + PhoneNumber_inst.medium + ' message ' + str(self.message) + ' to ' + str(PhoneNumber_inst) + '...' )

                applescript_Path = kabbes_imessage.mediums[ PhoneNumber_inst.medium ]

                try:
                    os.system( 'osascript {} {} "{}"'.format( applescript_Path.p, PhoneNumber_inst.formatted, self.message )  )
                except:
                    success = False
        else:
            print ('You are not on a Mac, cannot send iMessages')
            success = False

        return success
