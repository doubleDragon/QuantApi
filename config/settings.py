# coding=utf-8
from decouple import config

# 读取所有的key和secret
BFX_API_KEY = config('BFX_API_KEY')
BFX_API_SECRET = config('BFX_API_SECRET')
POLONIEX_API_KEY = config('POLONIEX_API_KEY')
POLONIEX_API_SECRET = config('POLONIEX_API_SECRET')