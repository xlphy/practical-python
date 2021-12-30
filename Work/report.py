# report.py
#
# Exercise 2.4
# read current prices and compute portfolio current values and loss/gain

import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        port = fileparse.parse_csv(f, types=[str, int, float], select=['name', 'shares', 'price'])
    return Portfolio([Stock(d['name'], d['shares'], d['price']) for d in port])

def read_prices(filename):
    with open(filename, 'rt') as f:
        prices = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    return dict(prices)

def calc_loss_gain(portfolio_filename, price_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(price_filename)
    cur_value = 0
    pnl = 0
    for holding in portfolio:
        cur_value += prices[holding.name] * holding.shares
        pnl += holding.shares * (prices[holding.name] - holding.price)
    return cur_value, pnl

def make_report(portfolio, prices):
    ''' portfolio: a list of dict, represent holdings
        prices: a dict record current prices of stocks
    return: a list of tuples, symbol name, shares, current price, price change
    '''
    report = []
    for pos in portfolio:
        report.append((pos.name, pos.shares, prices[pos.name], prices[pos.name] - pos.price))
    return report

def print_report(reportdata, formatter):
    '''format output'''
    # print headings
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    # print rowdata
    for name, shares, price, change in reportdata:
        p = f"${price:.2f}"
        rowdata = [name, str(shares), p, f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f"Usage: {argv[0]} " "portfile pricefile fmt")
    portfile, pricefile, fmt = argv[1], argv[2], argv[3]
    portfolio_report(portfile, pricefile, fmt)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)

