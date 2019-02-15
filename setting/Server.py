
from lib.Singleton import *
import lib.NetGeter as NetGeter

class Server(Singleton):
    
    server_list = []

    def __Singleton_Init__(self):
        self.server_list = NetGeter.get_json("https://raw.githubusercontent.com/cxwithyxy/weiruanshichuangxitongjihuogongju/master/config/server_list.json")
        
    def get_default_server(self):
        for i in self.server_list:
            try:
                if i["default"]:
                    return i["ip"]
            except:
                pass
        return self.server_list[0]["ip"]
