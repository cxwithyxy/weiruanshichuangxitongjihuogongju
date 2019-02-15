from setting.Key import Key 
from setting.Server import Server 
from lib.Systeminfo import Systeminfo 
import sys

reload(sys)
sys.setdefaultencoding( "gbk" )

# print Key().key_list
# print Key()
# print Server().server_list
# print Server().get_default_server()

print Systeminfo().get_windows_version_name()