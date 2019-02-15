#coding:utf-8

import requests

def get_json(url):
    return requests.get(url).json()