#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    # Split the line into fields
    fields = line.strip().split()
    
    # Convert the field to a float and emit it with a count of 1
    for field in fields:
        print "{0}\t{1}\t{2}".format("total", float(field), 1)