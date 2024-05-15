#!/usr/bin/python3
"""This module reads stdin line by line and executes metrics"""
import sys
import re
pattern = (r'^(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 '
           r'HTTP/1.1" (\d+) (\d+)$')
i = 0
total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            ip_address, date, status_code, file_size = match.groups()
            file_size = int(file_size)
            if status_code in status_codes:
                status_codes[status_code] += 1
            i += 1
            total_size += file_size
            if i % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print("{} : {}".format(code, status_codes[code]))
                        status_codes[code] = 0
except KeyboardInterrupt:
    print("\nFile Size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{} : {}".format(code, status_codes[code]))
    sys.exit(1)
