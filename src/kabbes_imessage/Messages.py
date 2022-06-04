from parent_class import ParentPluralList
import kabbes_imessage

class Messages( ParentPluralList ):

    def __init__( self ):
        ParentPluralList.__init__( self, 'Messages' )

    def make_Message( self, *args, **kwargs ):

        new_Message = kabbes_imessage.Message( *args, **kwargs ) 
        self._add( new_Message )
        return new_Message

    def send( self, **kwargs ):
        
        success = True
        for Message_inst in self:
            if not Message_inst.send( **kwargs ):
                success = False
        
        return success