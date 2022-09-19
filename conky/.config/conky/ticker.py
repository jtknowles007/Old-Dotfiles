#! /usr/bin/env python3

import datetime
import holidays
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
        symbol = '${color 00FF00}'
    elif diffprice <0:
        symbol = '${color FF0000}'
    else:
        symbol = '${color FFFFFF}'
    return [currentprice,symbol,diffprice]

def getstocks():
    stocklist = ['^DJI','^IXIC','^GSPC']
    dji = stock(stocklist[0])
    ndq = stock(stocklist[1])
    sp5 = stock(stocklist[2])

    #output stock data in conky format
    print("${{color}}DJIA${{goto 170}}${{alignr}}{:,}${{goto 245}}${{alignr}}{}{:+g}${{color}}".format(dji[0],dji[1],dji[2]))
    print("${{color}}NASDAQ${{goto 170}}${{alignr}}{:,}${{goto 245}}${{alignr}}{}{:+g}${{color}}".format(ndq[0],ndq[1],ndq[2]))
    print("${{color}}S&P 500${{goto 170}}${{alignr}}{:,}${{goto 245}}${{alignr}}{}{:+g}${{color}}".format(sp5[0],sp5[1],sp5[2]))

    #output stock data to text file for off hours
    header = "NAME\tVALUE\tCHANGE\n"
    dji_out = "DJIA\t{:,}\t{:+g}\n".format(dji[0],dji[2])
    ndq_out = "NASDAQ\t{:,}\t{:+g}\n".format(ndq[0],ndq[2])
    sp5_out = "S&P 500\t{:,}\t{:+g}".format(sp5[0],sp5[2])

    with open("/home/john/.config/conky/output.txt", "w") as file:
        file.write(header + dji_out + ndq_out + sp5_out)
        file.close

def offhours():
    with open("/home/john/.config/conky/output.txt", "r") as stocks:
        tsv_reader = csv.DictReader(stocks, delimiter="\t")
        for stock_index in tsv_reader:
            print("${{color6}}{}${{goto 170}}${{alignr}}{}${{goto 245}}${{alignr}}{}${{color}}".format(stock_index["NAME"],stock_index["VALUE"],stock_index["CHANGE"]))

def main():
    date_now = datetime.datetime.now()
    day_number = date_now.weekday()
    time_now = datetime.datetime.now().time()
    time_open = datetime.time(9,30,0)
    time_close = datetime.time(16,0,0)
    us_holidays = holidays.US()

    # Weekday, Non-Holiday, between market open and close?  Run the current stocks.  Othewise, display closing numbers
    if day_number <5 and date_now not in us_holidays and time_now >= time_open and time_now <= time_close:
        getstocks()
    else:
        offhours()

# if __name__ == "__main__":
main()
