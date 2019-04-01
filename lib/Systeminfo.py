#coding:utf-8

from lib.Singleton import *
import os
import re
import lib.myCmd as mycmd

class Systeminfo(Singleton):
    
    info_text = ""
    
    def __Singleton_Init__(self):
        self.info_text = mycmd.run_cmd("systeminfo")

    def get_windows_version_name(self):
        matchObj = re.search( u'OS 名称.*$', self.info_text, re.M)
        if matchObj:
            os_name_text = matchObj.group()
            os_name = re.search( u'.{2}版$', os_name_text, re.M)
            if os_name:
                return os_name.group()
        return False