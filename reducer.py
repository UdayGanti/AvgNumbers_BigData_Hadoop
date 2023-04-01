#!/usr/bin/env python
"""reducer.py"""

import sys

total = 0
count = 0

for line in sys.stdin:
    # Split the line into fields
    key, value, cnt = line.strip().split("\t")
    
    # Update the sum and count
    total += float(value)
    count += int(cnt)

# Calculate the mean
mean = total / count

# Emit the mean
print mean