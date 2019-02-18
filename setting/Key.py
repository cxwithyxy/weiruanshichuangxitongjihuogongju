
from lib.Singleton import *
import lib.NetGeter as NetGeter

class Key(Singleton):
    
    key_list = []

    def __Singleton_Init__(self):
        self.key_list = NetGeter.get_json("https://raw.githubusercontent.com/cxwithyxy/weiruanshichuangxitongjihuogongju/master/config/key_list.json")
        pass

    def get_key(self, window_version_name):
        return self.key_list[window_version_name][0]