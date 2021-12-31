# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    
    lines: file-like objects, iterables except str
    select: select a sub columns in headers
    types: convert row (string) to supplied data types
    has_headers: if the first line of the file is headers or not
    delimiter: specify separator, default is ','
    silence_errors: whether to silence errors that do not prevent execution

    return: a list of dicts (has_headers=True) or tuples (has_headers=False)
    '''
    if isinstance(lines, str):
        raise ValueError("lines can't be a string!")
    rows = csv.reader(lines, delimiter=delimiter)
    # read the file headers
    headers = next(rows) if has_headers else []
   
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
                log.warning("Row %d: Couldn't convert %s", rowno, row)
                log.debug("Row %d: Reason %s", rowno, e)
    return records

