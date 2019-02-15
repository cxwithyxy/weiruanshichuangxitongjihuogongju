#coding:utf-8

import requests
from os.path import join, abspath

requests.utils.DEFAULT_CA_BUNDLE_PATH = join(abspath('.'), 'cacert.pem')
requests.adapters.DEFAULT_CA_BUNDLE_PATH = join(abspath('.'), 'cacert.pem')

def get_json(url):
    return requests.get(url).json()