# report.py
#
# Exercise 2.4
# read current prices and compute portfolio current values and loss/gain

import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(filename, types=[str, int, float], select=['name', 'shares', 'price'])

def read_prices(filename):
    return dict(fileparse.parse_csv(filename, types=[str,float], has_headers=False))

def calc_loss_gain(portfolio_filename, price_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(price_filename)
    cur_value = 0
    pnl = 0
    for holding in portfolio:
        cur_value += prices[holding['name']] * holding['shares']
        pnl += holding['shares'] * (prices[holding['name']] - holding['price'])
    return cur_value, pnl

def make_report(portfolio, prices):
    ''' portfolio: a list of dict, represent holdings
        prices: a dict record current prices of stocks
    return: a list of tuples, symbol name, shares, current price, price change
    '''
    report = []
    for pos in portfolio:
        report.append((pos['name'], pos['shares'], prices[pos['name']], prices[pos['name']] - pos['price']))
    return report

def print_report(report):
    '''format output'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print("%10s %10s %10s %10s" % headers)
    print(('-'*10 + ' ') * len(headers))
    for name, shares, price, change in report:
        p = f"${price:.2f}"
        print(f"{name:>10s} {shares:>10d} {p:>10s} {change:>10.2f}")

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f"Usage: {argv[0]} " "portfile pricefile")
    portfile, pricefile = argv[1], argv[2]
    portfolio_report(portfile, pricefile)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)

