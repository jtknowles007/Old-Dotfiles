#! /usr/bin/env python3

# Getting an error?  Check for latest version of yfinance

import datetime
import holidays
import yfinance as yf
import csv

def stock(symbol):
    if symbol =="^DJI":
        shortname = "DJIA"
    elif symbol == "^IXIC":
        shortname = "NASDAQ"
    else:
        shortname = "S&P 500"

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
    currentprice = ("{:,}".format(currentprice))
    currentprice = str(currentprice)
    currentprice = currentprice.rjust(6," ")
    return [shortname,currentprice,symbol,diffprice]

def getstocks():
    stocklist = ['^DJI','^IXIC','^GSPC']
    header = "NAME\tVALUE\tCHANGE\n"
    stockstring = ""
    with open("/home/john/.config/conky/output.txt", "w") as file:
        file.write(header)
        for list in stocklist:
            stockresult = stock(list)

            #output stock data in conky format
            print("${{color}}{}${{goto 165}}{}${{goto 245}}${{alignr}}" \
                  "{}{:+g}${{color}}".format(stockresult[0],stockresult[1], \
                                             stockresult[2],stockresult[3]))

            #output stock data to text file for off hours
            file.write("{}\t{}\t{:+g}\n".format(stockresult[0], \
                                                stockresult[1],stockresult[3]))
        file.close

def offhours():
    with open("/home/john/.config/conky/output.txt", "r") as stocks:
        tsv_reader = csv.DictReader(stocks, delimiter="\t")
        for stock_index in tsv_reader:
            print("${{color6}}{}${{goto 160}}{}${{goto 245}}${{alignr}}{}" \
                  "${{color}}".format(stock_index["NAME"], \
                                      stock_index["VALUE"], \
                                      stock_index["CHANGE"]))

def main():
    date_now = datetime.datetime.now()
    day_number = date_now.weekday()
    time_now = datetime.datetime.now().time()
    time_open = datetime.time(9,30,0)
    time_close = datetime.time(16,0,0)
    us_holidays = holidays.US()

    # Weekday, Non-Holiday, between market open and close?
    # Run the current stocks.  Otherwise, display closing numbers
    if day_number <5 and date_now not in us_holidays and time_now >= \
       time_open and time_now <= time_close:
        getstocks()
    else:
        offhours()

# if __name__ == "__main__":
main()
