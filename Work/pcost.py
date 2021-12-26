# pcost.py
#
# Exercise 1.27
# read Data/portfolio.csv to calculate total cost

def portfolio_cost2(filename):
    "calculate the cost of a portfolio given by filename in Data folder"
    total = 0
    f = open(f"Data/{filename}", 'rt')
    headers = next(f)
    for line in f:
        try: 
            row = line.split(',')
            total += int(row[1]) * float(row[2])
        except ValueError:
            print(f"parse line: {line} failed, skip to the next.")
    f.close()
    return total

import csv
def portfolio_cost(csv_filename):
    "calculate the cost of a portfolio given by filename in Data folder"
    f = open(f"Data/{csv_filename}")
    rows = csv.reader(f)
    headers = next(rows)
    total = 0
    for r in rows:
        try:
            total += int(r[1]) * float(r[2])
        except ValueError:
            print(f"parse row with csv.reader failed, row={r}, skip to the next.") 
    f.close()
    return total

import sys
# be able to pass a filename as an argument to a script
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost:", cost)

