#coding:utf-8

from setting.Key import Key 
from setting.Server import Server 
from lib.Systeminfo import Systeminfo 
import sys
import os

def runCmd(cmd):
    os.system(cmd)
    pass

print( u"获取系统版本...")

window_version_name = Systeminfo().get_windows_version_name()
print( u"当前版本是: " + window_version_name)

print( u"获取注册码...")
reg_code = Key().get_key(window_version_name)
print( u"适配注册码为: " + reg_code)

print( u"获取注册服务器...")
server_ip = Server().get_default_server()
print( u"适配注册服务器为: " + server_ip)

print( u"卸载系统已经存在的注册码")
runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /upk")
print( u"把注册码 " + reg_code + u" 写入系统")
runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /ipk " + reg_code)
print( u"设置注册服务器")
runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /skms " + server_ip)

print( u"进行注册")
runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /ato")
print( u"注册完毕")

input(u"按下回车键结束运行")