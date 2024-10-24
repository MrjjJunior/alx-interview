#!/usr/bin/python3
''' Python script that reads stdin '''
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
    500: 0
}
line_count = 0


def log_stats():
    ''' Prints the log stats '''
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        if status_codes_count[status_code] > 0:
            print(f"{status_code}: {status_codes_count}")


try:
    for line in sys.stdin:
        line_count = line_count + 1

    regex = r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    exptd_fomat = re.match(regex, line)
    if exptd_fomat:
        status_code = int(exptd_fomat.group(3))
        file_size = int(exptd_fomat.group(4))

        total_file_size = total_file_size + file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

    if line_count % 10 == 0:
        log_stats()


except KeyboardInterrupt:
    log_stats()
