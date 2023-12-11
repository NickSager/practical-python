# fileparse.py
#
# Exercise 8.2
import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True,
              delimiter=',', silence_errors=False):
    '''
    Parses lines from a CSV file into a list of records
    Takes only lines from a file - allows flexibility of opening differently
    Typical useage:
        with open('file.csv') as f:
            x = parse_csv(f)
    Note: types needs to match select or row in length
        Implement error handling here later
    '''
    if select and not has_headers:
        raise RuntimeError('Select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

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
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                    # print(f"Row {rowno}: Couldn't convert {row}")
                    # print(f"Row {rowno}: Reason {e}")
                    continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records