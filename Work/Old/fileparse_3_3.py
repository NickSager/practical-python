# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True,
              delimiter=',', silence_errors=False):
    '''
    Parses a CSV file into a list of records
    Note: types needs to match select or row in length
        Implement error handling here later
    '''
    if select and not has_headers:
        raise RuntimeError('Select argument requires column headers')
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:  # Skip rows with no data "Truthiness"
                continue

            if select:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")

            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
