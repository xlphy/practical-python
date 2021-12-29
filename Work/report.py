# report.py
#
# Exercise 2.4
# read current prices and compute portfolio current values and loss/gain

import csv

def read_portfolio(filename):
    portfolio = [] # list of tuples
    with open(f"Data/{filename}", 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #symbol name, number of shares, price
            try:
                portfolio.append((row[0], int(row[1]), float(row[2])))
            except Exception as e:
                print(f"parsing row has errors, skip it, row = {row}, error = {e}")
    return portfolio

def read_portfolio_dict(filename):
    portfolio = [] # list of dicts
    with open(f"Data/{filename}", 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                holding = dict(zip(headers, row))
                holding['shares'] = int(holding['shares'])
                holding['price'] = float(holding['price'])
                portfolio.append(holding)
            except Exception as e:
                print(f"parsing row has errors, skip it, row = {row}, error = {e}")
    return portfolio

def read_prices(filename):
    prices = {}
    with open(f"Data/{filename}", 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception as e:
                print(f"parsing row has errors, skip it, row = {row}, error = {e}")
    return prices

def calc_loss_gain(portfolio_filename, price_filename):
    portfolio = read_portfolio_dict(portfolio_filename)
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

# format output
portfolio = read_portfolio_dict('portfolio.csv')
prices = read_prices('prices.csv')

data = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')

print("%10s %10s %10s %10s" % headers)
print(('-'*10 + ' ') * len(headers))
for name, shares, price, change in data:
   # print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")
   # add '$' in front of price
    p = f"${price:.2f}"
    print(f"{name:>10s} {shares:>10d} {p:>10s} {change:>10.2f}")

