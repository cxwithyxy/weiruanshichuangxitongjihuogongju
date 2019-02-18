#coding:utf-8

from setting.Key import Key 
from setting.Server import Server 
from lib.Systeminfo import Systeminfo 
import sys
import os

reload(sys)
sys.setdefaultencoding( "gbk" )

def runCmd(cmd):
    os.system(cmd)
    pass

print u"获取系统版本..."

window_version_name = Systeminfo().get_windows_version_name()
print u"当前版本是: " + window_version_name

print u"获取注册码..."
reg_code = Key().get_key(window_version_name)
print u"适配注册码为: " + reg_code

print u"获取注册服务器..."
server_ip = Server().get_default_server()
print u"适配注册服务器为: " + server_ip

# slmgr /upk
# slmgr /ipk xxxxx-xxxxx-xxxxx-xxxxx-xxxxx（激活密匙）
# slmgr /skms kms.xspace.in
# slmgr /ato
print u"卸载系统已经存在的注册码"
runCmd("slmgr /upk")
print u"把注册码 " + reg_code + u" 写入系统"
runCmd("slmgr /ipk " + reg_code)
print u"设置注册服务器"
runCmd("slmgr /skms " + server_ip)

print u"进行注册"
runCmd("slmgr /ato")
print u"注册完毕"