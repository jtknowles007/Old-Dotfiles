#! /usr/bin/env python3

import datetime
import pytz
from pytz import timezone
import yfinance as yf
import csv

def stock(symbol):
    lookup = yf.Ticker(symbol)
    quoteprice = lookup.info['regularMarketPrice']
    openprice = lookup.info['previousClose']
    if quoteprice >=1:
        currentprice = round(quoteprice)
        diffprice = round(quoteprice - openprice)
    else:
        currentprice = round(quoteprice,3)
        diffprice = round((quoteprice - openprice,3))
    if diffprice >0:
        symbol = '${color 009900}  '
    elif diffprice <0:
        symbol = '${color 990000}  '
    else:
        symbol = ' '
    return [currentprice,symbol,diffprice]

def getstocks():
    stocklist = ['^DJI','^IXIC','^GSPC']
    dji = stock(stocklist[0])
    ndq = stock(stocklist[1])
    sp5 = stock(stocklist[2])

    print("${{color}}DJIA:${{goto 160}}{:,}${{font Font Awesome 6 Free Solid:size=10}}${{goto 235}}{}${{font}}${{color}}${{voffset -1}}${{alignr}}{:,}".format(dji[0],dji[1],dji[2]))
    print("${{color}}NASDAQ:${{goto 160}}{:,}${{font Font Awesome 6 Free Solid:size=10}}${{goto 235}}{}${{font}}${{color}}${{voffset -1}}${{alignr}}{:,}".format(ndq[0],ndq[1],ndq[2]))
    print("${{color}}S&P 500:${{goto 160}}{:,}${{font Font Awesome 6 Free Solid:size=10}}${{goto 235}}{}${{font}}${{color}}${{voffset -1}}${{alignr}}{:,}".format(sp5[0],sp5[1],sp5[2]))

def offhours():
    print("Markets Closed")
    with open("/home/john/.config/conky/output.txt", "r") as stocks:
        tsv_reader = csv.DictReader(stocks, delimiter="\t")
        for stock_index in tsv_reader:
            print("${{color6}}{}${{goto 170}}{}${{goto 245}}${{alignr}}{}${{color}}".format(stock_index["NAME"],stock_index["VALUE"],stock_index["CHANGE"]))
def main():
    time_now = datetime.datetime.now().time()
    time_open = datetime.time(9,30,0)
    time_close = datetime.time(16,0,0)

    if time_now >= time_open and time_now <= time_close:
        getstocks()
    else:
        offhours()

# if __name__ == "__main__":
main()
