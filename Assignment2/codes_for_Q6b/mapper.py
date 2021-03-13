#!/usr/bin/env python
# this python file extract the event information for the reducer to generate traces
import sys

# input comes from STDIN
for line in sys.stdin:
	# remove whitespace and split row into values
    line_split = line.strip().split("\t")
    # assign case, activity, timestamp
    case = line_split[0]
    activity = line_split[2]
    timestamp = line_split[1]
    # write the results to STDOUT;
    # key: case, value: (timestamp,activity)
    print('%s-%s\t%s' % (case, timestamp, activity))