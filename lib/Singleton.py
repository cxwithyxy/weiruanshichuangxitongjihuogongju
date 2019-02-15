#coding:utf-8
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = object.__new__(cls)
                    cls._instance.__Singleton_Init__(*args, **kwargs)
        return cls._instance

    def __Singleton_Init__(self):
        raise RuntimeError("__Singleton_Init__ must be overwritten")