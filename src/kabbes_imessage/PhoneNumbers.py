from parent_class import ParentPluralList
from kabbes_imessage import PhoneNumber

class PhoneNumbers( ParentPluralList ):

    def __init__( self ):
        ParentPluralList.__init__( self )

    def _add_PhoneNumber( self, new_PhoneNumber ):

        self._add( new_PhoneNumber )
        
    def make_PhoneNumber( self, *args, **kwargs ):

        new_PhoneNumber = PhoneNumber( *args, **kwargs )
        self._add_PhoneNumber( new_PhoneNumber )
        return new_PhoneNumber
