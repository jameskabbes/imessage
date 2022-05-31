import Parent_Class
import py_starter as ps
import imessage_support_functions as imsf

class Message( Parent_Class.Parent_Class ):

    DEFAULT_ATT_VALUES = {
    'default_medium': 'iMessage',
    'mediums': []
    }

    def __init__( self, text, PhoneNumbers, **kwargs ):

        Parent_Class.Parent_Class.__init__( self )

        kwargs = ps.replace_default_kwargs( Message.DEFAULT_ATT_VALUES, **kwargs )
        self.set_atts( kwargs )

        self.text = str(text)
        self.PhoneNumbers = PhoneNumbers
        self.get_mediums()

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = [ 'type','PhoneNumber' ], **kwargs )

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['text','PhoneNumber','medium'], **kwargs )

    def get_mediums( self ):

        if len(self.mediums) != len(self.PhoneNumbers):
            self.mediums = [ self.default_medium, ] * len(self.medium)

    def send( self, **kwargs ):

        success = True

        for i in range(len(self.PhoneNumbers)):

            PhoneNumber_inst = self.PhoneNumbers[i]
            medium = self.mediums[i]

            if medium == 'iMessage':
                if not imsf.send_imessage( PhoneNumber_inst.digits, self.text, **kwargs ):
                    success = False

            else:
                if not imsf.send_sms( PhoneNumber_inst.digits, self.text, **kwargs ):
                    success = False

        return success
