# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    
    select: select a sub columns in headers
    types: convert row (string) to supplied data types
    has_headers: if the first line of the file is headers or not
    delimiter: specify separator, default is ','
    silence_errors: whether to silence errors that do not prevent execution

    return: a list of dicts (has_headers=True) or tuples (has_headers=False)
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # read the file headers
        if has_headers:
            headers = next(rows)
        else:
            headers = []
        if select:
            if not headers:
                raise RuntimeError("select argument requires column headers")
            # find selected column names indices
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for rowno, row in enumerate(rows, start=1):
            if not row:  # skip rows with no data
                continue
            try:
                if indices:
                    row = [row[index] for index in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if headers:
                    # make a dictionary
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)    
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert row {row}\nRow {rowno}: Reason {e}")
    return records


