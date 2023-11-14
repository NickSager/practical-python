#!/usr/bin/env python3
# ticker.py

from .follow import follow
import csv


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    # for row in rows:
    #     yield dict(zip(headers, row))
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile, logfile, fmt):
    '''
    Watches a logfile for events matching stocks in a portfolio and outputs
    the Name, Price, and Change in a specified format using the tableformatter
    module.
    '''
    import report
    import tableformat

    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    # rows = filter_symbols(rows, portfolio)

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([row['name'],
                       f"{row['price']:0.2f}",
                       f"{row['change']:0.2f}"])


def main(args):
    # Default values for arguments
    default_portfoliofile = 'Data/portfolio.csv'
    default_logfile = 'Data/stocklog.csv'
    default_fmt = 'txt'

    # Use the default arguments if not provided
    portfoliofile = args[1] if len(args) > 1 else default_portfoliofile
    logfile = args[2] if len(args) > 2 else default_logfile
    fmt = args[3] if len(args) > 3 else default_fmt

    # Now call the ticker function with the arguments
    ticker(portfoliofile, logfile, fmt)


if __name__ == "__main__":
    import sys
    main(sys.argv)
