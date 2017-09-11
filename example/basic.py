from bitfinex.client import Client

client = Client()

symbols = client.symbols()
print(symbols)

symbol = 'ltcusd'

ticker = client.ticker(symbol)
if ticker is not None:
    print(str(ticker))

# print(client.today(symbol))
# print(client.stats(symbol))

# parameters = {'limit_asks': 2, 'limit_bids': 2}
#
# print(client.lendbook('btc', parameters))
# print(client.order_book(symbol, parameters))
