#!/usr/bin/env python3
# report.py
#
# Updated to use fileparse.py rather than manually reading csv
# Exercise 3.12
from fileparse import parse_csv


def read_portfolio(filename, select=['name', 'shares', 'price'],
                   types=[str, int, float], has_headers=True, delimiter=',',
                   silence_errors=False):
    '''
    Read a stock portfolio file into a list of dictionaries with items
    name, shares, and price.
    '''
    with open(filename) as file:
        portfolio = parse_csv(file, select=select, types=types,
                              has_headers=has_headers, delimiter=delimiter,
                              silence_errors=silence_errors)
    return (portfolio)


def read_prices(filename, select=None, types=[str, float], has_headers=False,
                delimiter=',', silence_errors=False):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as file:
        prices = parse_csv(file, select=select, types=types,
                           has_headers=has_headers, delimiter=delimiter,
                           silence_errors=silence_errors)
    prices = dict(prices)
    return (prices)


def make_report(portfolio, prices):
    '''Create a report from a list of portfolio holdings.'''
    report = []
    for holding in portfolio:
        current_price = prices[holding['name']]
        change = current_price - holding['price']
        summary = (holding['name'], holding['shares'], current_price, change)
        report.append(summary)
    return (report)


def print_report(report, portfolio, prices):
    '''
    Print a nicely formated table from a list of (name, shares, price, change)
    takes a report object, portfolio, and prices.
    '''
    # Update the Gain/Loss and compute the total value
    total_value = 0.0
    orig_value = 0.0
    for holding in portfolio:
        total_value += holding['shares'] * prices[holding['name']]
        orig_value += holding['shares'] * holding['price']
        holding['change'] = holding['shares'] * (
                prices[holding['name']] - holding['price'])

    # Print the report using f-strings

    # Header
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f"{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}")
    print(("-" * 10 + " ") * len(headers))

    # Table Body
    for name, shares, price, change in report:
        print(f"{name:>10} {shares:>10} {price:>10.2f} {change:>10.2f}")

    # Separator and Footer
    print('-' * 10 + ' ' * (len(headers) - 1))
    print(f"{'':>10} {'':>10} {'Total':>10} {total_value:>10.2f}")
    print(f"{'':>10} {'':>10} {'Change':>10} {total_value - orig_value:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    '''Make a stock report given portfolio and prices files.'''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report, portfolio, prices)


def main(argv):
    if len(argv) == 2:
        portfolio_filename = argv[1]
        prices_filename = 'Data/prices.csv'
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'

    portfolio_report(portfolio_filename, prices_filename)


if __name__ == "__main__":
    import sys
    main(sys.argv)
