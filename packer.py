from distutils.core import setup
import py2exe

# see https://www.cnblogs.com/hanson1/articles/7101578.html

setup(
    options = { 
        "py2exe": { 
            "dll_excludes": ["MSVCP90.dll"], 
            "bundle_files": 1,
            "compressed": 1,
            "optimize": 2
        }
    },
    data_files = [("",["./../cacert.pem"])],
    zipfile = None,
    console = [{"script": "./../index.py"}]
)