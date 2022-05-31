import os
import sys
import dir_ops as do #module found in Analytics-Packages
from dir_ops import Path #custom classes found in Analytics-Packages
from dir_ops import Dir #custom classes found in Analytics-Packages

params_Path = Path( os.path.abspath(__file__) )
repo_Dir = Dir( params_Path.ascend() )

send_imessage_script_Path = Path( repo_Dir.join( 'send_imessage.applescript' ) )
send_sms_script_Path = Path( repo_Dir.join( 'send_sms.applescript' ) )
