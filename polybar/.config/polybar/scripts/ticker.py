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
        symbol = '${color 009900}  ${color 4F4F4F}'
    elif diffprice <0:
        symbol = '${color 990000}  ${color 4F4F4F}'
    else:
        symbol = 'NC'
    return [currentprice,symbol,diffprice]

def main():
    stocklist = ['^DJI','^IXIC','^GSPC']
    dji = stock(stocklist[0])
    ndq = stock(stocklist[1])
    sp5 = stock(stocklist[2])

    print("DJIA:{:,}${{font Font Awesome 6 Free Solid:size=11}}{}${{font}}${{voffset -1}}{:,} NASDAQ:{:,}${{font Font Awesome 6 Free Solid:size=11}}{}${{font}}${{voffset -1}}{:,} S&P 500:{:,}${{font Font Awesome 6 Free Solid:size=11}}{}${{font}}${{voffset -1}}{:,}".format(dji[0],dji[1],dji[2],ndq[0],ndq[1],ndq[2],sp5[0],sp5[1],sp5[2]))

if __name__ == "__main__":
    main()
