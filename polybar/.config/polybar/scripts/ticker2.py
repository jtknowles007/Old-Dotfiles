#! /usr/bin/env python3

from datetime import datetime, time
import yfinance as yf
def stock(symbol):
    lookup = yf.Ticker(symbol)
    quoteprice = lookup.info['regularMarketPrice']
    openprice = lookup.info['previousClose']
    if quoteprice >=1:
        currentprice = round(quoteprice)
        diffprice = abs(round(quoteprice - openprice))
    else:
        currentprice = round(quoteprice,3)
        diffprice = round((quoteprice - openprice,3))
    if diffprice >0:
        symbol = '${color 009900}  ${color1}'
    elif diffprice <0:
        symbol = '${color 990000}  ${color1}'
    else:
        symbol = ' '
    return [currentprice,symbol,diffprice]

def main():
    stocklist = ['^DJI','^IXIC','^GSPC']
    dji = stock(stocklist[0])
    ndq = stock(stocklist[1])
    sp5 = stock(stocklist[2])

    print("DJIA:${{goto 150}}{:,}${{font Font Awesome 6 Free Solid:size=20}}${{goto 245}}{}${{font}}${{voffset -1}}{:,}".format(dji[0],dji[1],dji[2]))
    print("NASDAQ:${{goto 150}}{:,}${{font Font Awesome 6 Free Solid:size=20}}${{goto 245}}{}${{font}}${{voffset -1}}{:,}".format(ndq[0],ndq[1],ndq[2]))
    print("S&P 500:${{goto 150}}{:,}${{font Font Awesome 6 Free Solid:size=20}}${{goto 245}}{}${{font}}${{voffset -1}}{:,}".format(sp5[0],sp5[1],sp5[2]))

    header = "NAME\tVALUE\tCHANGE\n"
    dji_out = "DJIA\t{:,}\t{:+g}\n".format(dji[0],dji[2])
    ndq_out = "NASDAQ\t{:,}\t{:+g}\n".format(ndq[0],ndq[2])
    sp5_out = "S&P 500\t{:,}\t {:+g}".format(sp5[0],sp5[2])

    file = open("output.txt", "w")
    file.write(header + dji_out + ndq_out + sp5_out)
    file.close

if __name__ == "__main__":
    main()
