# coding=utf-8
from bitfinex.client import TradeClient

# from decouple import config
#
# API_KEY = config('API_KEY')
# API_SECRET = config('API_SECRET')

from config import settings

# print('API_KEY=' + settings.BFX_API_KEY)
# print('API_SECRET=' + settings.BFX_API_SECRET)

api_key = settings.BFX_API_KEY
api_secret = settings.BFX_API_SECRET

tradeClient = TradeClient(api_key, api_secret)

symbol = 'eosusd'
amount = '0.1'
price = '15.0'
side = 'sell'
# 这个地方如果带了exchange那就是exchange 单，如果没带就是margin单
order_type = 'exchange limit'

order_id = tradeClient.place_order(amount=amount, price=price, side=side, ord_type=order_type,
                                   symbol=symbol)

print("place order: " + str(order_id))


