#coding:utf-8

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

print u"获取系统版本..."

window_version_name = Systeminfo().get_windows_version_name()
print u"当前版本是: " + window_version_name

print u"获取注册码..."
reg_code = Key().get_key(window_version_name)
print u"适配注册码为: " + reg_code