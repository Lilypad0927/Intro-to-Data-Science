#!/usr/bin/env python
import sys
# the input is from the log file
# the output includes case, timestamp, activity and service time without merge event with the same caseid

# input comes from STDIN
for line in sys.stdin:
    # remove whitespace and split row into values
    line_split = line.strip().split("\t")
    # assign case, activity, timestamp
    case = line_split[0]
    activity = line_split[2]
    timestamp = line_split[1]
    service_time = line_split[-1]
    # write the results to STDOUT;
    # key: case, value: (timestamp,activity)
    print('%s-%s\t%s\t%s' % (case, timestamp, activity, service_time))