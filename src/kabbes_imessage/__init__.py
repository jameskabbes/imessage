import platform

ON_MAC = (platform.system() == 'Darwin')
if not ON_MAC:
    print ('kabbes_imessage Note: no messages will be able to send. You are not running this on a Macintosh system')

import dir_ops as do
import os

_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
_src_Dir = _Dir.ascend()                                  #src Dir that is one above
_repo_Dir = _src_Dir.ascend()                
_cwd_Dir = do.Dir( do.get_cwd() )

applescripts_Dir = _Dir.join_Dir( path = 'message_mediums' )
applescript_extension = '.applescript'

###
mediums_Paths = applescripts_Dir.list_contents_Paths( block_dirs=True )
mediums = {}
for medium_Path in mediums_Paths:
    mediums[ medium_Path.root ] = medium_Path


from .Message import Message
from .Messages import Messages
from .PhoneNumber import PhoneNumber
from .PhoneNumbers import PhoneNumbers

