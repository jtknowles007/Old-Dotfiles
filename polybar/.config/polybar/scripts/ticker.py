#! /usr/bin/env python3

from datetime import datetime, time
import yfinance as yf
def stock(symbol):
    lookup = yf.Ticker(symbol)
    quoteprice = lookup.info['regularMarketPrice']
    openprice = lookup.info['previousClose']
    if quoteprice >=1:
        currentprice = round(quoteprice)
        diffprice = round(quoteprice - openprice)
    else:
        currentprice = round(quoteprice,3)
        diffprice = round(quoteprice - openprice,3)
    if diffprice >0:
        symbol = ''
    elif diffprice <0:
        symbol = ''
    else:
        symbol = ' '
    return [currentprice,symbol,diffprice]

def main():
    stocklist = ['^DJI','^IXIC','^GSPC']
    dji = stock(stocklist[0])
    ndq = stock(stocklist[1])
    sp = stock(stocklist[3])

    print("DJIA: {:,} {} {:,} NASDAQ: {:,} {} {:,} S&P 500: {:,} {} {:,}".format(dji[0],dji[1],dji[2],ndq[0],ndq[1],ndq[2],sp[0],sp[1],sp[2]))

if __name__ == "__main__":
    main()
