#!/usr/bin/env python
import time

# This program buys some Ethereumcoins and sells them for a bigger price
from bittrex import bittrex

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('key', 'secret')

# Market to trade at
trade = 'USDT'
currency = 'ETH'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 100
# How big of a profit you want to make
multiplier = 1.1

#getorderbook(self, market, type, depth=20):
# Getting the USDT price for ETH
while True:
    localtime = time.asctime( time.localtime(time.time()) )
    ethsummary = api.getmarketsummary(market)
    ethprice = ethsummary[0]['Last']
    print '{0}: {1}/{2} {3:.2f}$'.format(localtime, currency, trade, ethprice)
    time.sleep(30)

## Buying 100 ETH for USDT
#print 'Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, ethprice, trade)
#api.buylimit(market, amount, ethprice)
#
## Multiplying the price by the multiplier
#ethprice = round(ethprice*multiplier, 8)
#
## Selling 100 ETH for the  new price
#print 'Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, ethprice, trade)
#api.selllimit(market, amount, ethprice)
#
## Gets the ETH balance
#ethbalance = api.getbalance(currency)
#print "Your balance is {0} {1}.".format(ethbalance['Available'], currency)

# For a full list of functions, check out bittrex.py or https://bittrex.com/Home/Api
