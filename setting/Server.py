
from lib.Singleton import *
import lib.NetGeter as NetGeter

class Server(Singleton):
    
    server_list = []

    def __Singleton_Init__(self):
        self.server_list = NetGeter.get_json("https://raw.githubusercontent.com/cxwithyxy/weiruanshichuangxitongjihuogongju/master/config/server_list.json")
        pass