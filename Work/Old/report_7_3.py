#!/usr/bin/env python3
# report.py
#
# Updated to use fileparse.py rather than manually reading csv
# Exercise 3.12
import fileparse
from stock import Stock
from portfolio import Portfolio
import tableformat


def read_portfolio(filename, select=['name', 'shares', 'price'],
                   types=[str, int, float], has_headers=True, delimiter=',',
                   silence_errors=False):
    '''
    Read a stock portfolio file into a list of dictionaries with items
    name, shares, and price.
    '''
    with open(filename) as file:
        portfolio_dict = fileparse.parse_csv(file, select=select, types=types,
                                             has_headers=has_headers,
                                             delimiter=delimiter,
                                             silence_errors=silence_errors)
    portfolio = [Stock(**d)
                 for d in portfolio_dict]
    return Portfolio(portfolio)


def read_prices(filename, select=None, types=[str, float], has_headers=False,
                delimiter=',', silence_errors=False):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as file:
        prices = fileparse.parse_csv(file, select=select, types=types,
                                     has_headers=has_headers, delimiter=delimiter,
                                     silence_errors=silence_errors)
    prices = dict(prices)
    return (prices)


def make_report_data(portfolio, prices):
    '''
    Create a report from a list of portfolio holdings.
    '''
    report = []
    for holding in portfolio:
        current_price = prices[holding.name]
        change = current_price - holding.price
        summary = (holding.name, holding.shares, current_price, change)
        report.append(summary)
    return (report)


def print_report(report, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change)
    takes a report object, portfolio, and prices.
    '''

    current_value = 0.0  # Can do here, or loop again in footer
    net_change = 0.0

    # Header
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])

    # Table Body
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
        # Iterate here or loop again in footer
        current_value += shares*price
        net_change += shares*change

    # Separator and Footer
    footer = {'Value': current_value, 'Net Change': net_change}
    formatter.footer(footer)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    fmt = 'txt', 'csv', 'html'
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report Data
    report = make_report_data(portfolio, prices)

    # Print the report
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    else:
        raise SystemExit('Usage: %s portfile pricefile format' % argv[0])


if __name__ == "__main__":
    import sys
    main(sys.argv)
