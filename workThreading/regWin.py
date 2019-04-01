# coding:utf-8

from setting.Key import Key 
from setting.Server import Server
from lib.Systeminfo import Systeminfo
from lib.Singleton import *

import threading
import os
import subprocess

class RegWin(Singleton):

    output_func = None

    def __Singleton_Init__(self, output_func = print):
        self.output_func = output_func
        pass

    def thread_do_reg(self):
        t = threading.Thread(target=self.do_reg)
        t.setDaemon(True)
        t.start()

    def do_reg(self):

        def runCmd(cmd):
            (result, output) = subprocess.getstatusoutput(cmd)
            self.output_func(output)
         
        self.output_func( u"获取系统版本...")
         
        window_version_name = Systeminfo().get_windows_version_name()
        self.output_func( u"当前版本是: " + window_version_name)
         
        self.output_func( u"获取注册码...")
        reg_code = Key().get_key(window_version_name)
        self.output_func( u"适配注册码为: " + reg_code)
         
        self.output_func( u"获取注册服务器...")
        server_ip = Server().get_default_server()
        self.output_func( u"适配注册服务器为: " + server_ip)
         
        self.output_func( u"卸载系统已经存在的注册码")
        runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /upk")
        self.output_func( u"把注册码 " + reg_code + u" 写入系统")
        runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /ipk " + reg_code)
        self.output_func( u"设置注册服务器")
        runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /skms " + server_ip)
         
        self.output_func( u"进行注册")
        runCmd("cscript //nologo c:/Windows/System32/slmgr.vbs /ato")
        self.output_func( u"注册完毕")
        self.output_func( u"您可以关闭该程序了")
