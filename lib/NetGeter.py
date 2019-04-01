#coding:utf-8

import requests
from os.path import join, abspath

def get_json(url):
    return requests.get(url).json()