#! /usr/bin/env python3

from datetime import datetime, time
import yahoo_fin.stock_info as yf
def stock(symbol):
    lookup = yf.get_quote_table(symbol, dict_result=True)
    quoteprice = lookup['Quote Price']
    openprice = lookup['Previous Close']
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
    stocklist = ['^DJI','^IXIC','DOGE-USD','^GSPC']
    dji = stock(stocklist[0])
    ndq = stock(stocklist[1])
    doge = stock(stocklist[2])
    sp = stock(stocklist[3])

    print("DJIA: {:,} {} {:,} NASDAQ: {:,} {} {:,} S&P 500: {:,} {} {:,}".format(dji[0],dji[1],dji[2],ndq[0],ndq[1],ndq[2],sp[0],sp[1],sp[2]))
    # print("DJIA: {:,} {} {:,} NASDAQ: {:,} {} {:,}".format(dji[0],dji[1],dji[2],ndq[0],ndq[1],ndq[2]))

if __name__ == "__main__":
    main()
