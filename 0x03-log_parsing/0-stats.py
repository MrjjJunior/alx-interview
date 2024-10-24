#!/usr/bin/python3
""" A python script """
import sys
import re

total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0


def print_stats():
    """Prints the statistics accumulated so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        regex = r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
        match = re.match(regex, line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_file_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        if line_count % 10 == 0:
            print_stats()

    print_stats()

except Exception:
    print_stats()
