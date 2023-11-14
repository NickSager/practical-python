# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

    def footer(self, footer):
        '''
        Emit a seperator and footer
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format (print)
    '''

    def headings(self, headers):
        self.headings = headers  # Test
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10+' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

    def footer(self, footer):
        print(('-'*10+' ') * (len(self.headings)))
        for name, value in footer.items():
            print((' '*10+' ') * (len(self.headings)-2), end='')
            print(f'{name:>10s}', end=' ')
            print(f'${value:>10,.2f}')


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    Note: Footer not working w/ dictionary. Fix later
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

    def footer(self, footer):
        pass


class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    Note: Footer not working w/ dictionary. Fix later
    '''

    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<td>{h}</td>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r}</td>', end='')
        print('</tr>')

    def footer(self, footer):
        pass


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
    return formatter


def print_table(data, colnames, formatter):
    '''
    Given records, a list of the desired column names, and a formatter,
    this function prints a table in the desired format
    '''
    # Header
    formatter.headings(colnames)

    # Table Body one line at a time
    for obj in data:
        rowdata = [str(getattr(obj, name)) for name in colnames]
        formatter.row(rowdata)
