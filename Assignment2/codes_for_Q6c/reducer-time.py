#!/usr/bin/env python
import sys
import json
# this file is to merge the information from mapper-time.py
# 1. merge the event with the same caseid
# 2. calculate the total service time for the trace.
current_case = None

# input comes from STDIN
for line in sys.stdin:
	# remove whitespace and parse the input (case,(timestamp, activity)) we got from mapper.py
	caseid_timestamp, activity, service_time = line.strip().split("\t")
	caseid = caseid_timestamp.strip().split("-")[0]
	# shuflling is done by Hadoop
	if caseid != current_case:
		# write result to STDOUT
		if current_case:
			print('%s\t%s\t%s' % (current_case,json.dumps(current_trace), sum_service_time))
		# reset current trace
		current_case = caseid
		current_trace = list()
		sum_service_time = 0
		current_trace += [activity]
		sum_service_time += int(service_time)
	else:
		current_trace += [activity]
		sum_service_time += int(service_time)
# output the last word
if current_case == caseid:
	print('%s\t%s\t%s' % (caseid,json.dumps(current_trace), sum_service_time))