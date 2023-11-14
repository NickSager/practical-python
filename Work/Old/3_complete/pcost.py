#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27, 1.32, 2.15, 3.14
from report import read_portfolio


def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total_cost = 0.0
    # This results in the errors being printed twice
    # parse_csv also throws error, but removing this causes program to fail.
    # Work on handling this more gracefully later
    for index, holding in enumerate(portfolio, start=1):
        try:
            nshares = int(holding['shares'])
            price = float(holding['price'])
            total_cost += nshares * price
        except ValueError:
            print(f'Row {index}: Couldn\'t Convert: {holding}')
    return (total_cost)


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print(f'Total cost: ${cost:0.2f}')


if __name__ == "__main__":
    import sys
    main(sys.argv)

# Old Version pre 3.14
# import sys
# import csv
#
#
# def portfolio_cost(filename):
#     total_cost = 0.0
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for index, line in enumerate(rows, start=1):
#             record = dict(zip(headers, line))
#             try:
#                 nshares = int(record['shares'])
#                 price = float(record['price'])
#                 total_cost += nshares * price
#             except ValueError:
#                 print(f'Row {index}: Couldn\'t Convert: {line}')
#     return (total_cost)
#
#
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'
#
# cost = portfolio_cost(filename)
# print(f'Total cost: ${cost:0.2f}')

# Old Version pre 2.15
# def portfolio_cost(filename):
#     total_cost = 0.0
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for line in rows:
#             try:
#                 nshares = int(line[1])
#                 price = float(line[2])
#                 total_cost += nshares * price
#             except ValueError:
#                 print('Bad row:', line)
#     return (total_cost)
#
#
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'
#
# cost = portfolio_cost(filename)
# print(f'Total cost: ${cost:0.2f}')
#

# Old Version pre 1.32
# def portfolio_cost(filename):
#     total_cost = 0.0
#     with open(filename, 'rt') as f:
#         headers = next(f).split(',')
#         for line in f:
#             try:
#                 row = line.split(',')
#                 nshares = int(row[1])
#                 price = float(row[2])
#                 total_cost += nshares * price
#             except ValueError:
#                 print('Bad row:', row)
#     return(total_cost)    
#     # print(f'Total cost: ${total_cost:0.2f}')
# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', cost)
