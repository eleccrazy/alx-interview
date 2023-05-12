#!/usr/bin/python3
"""
File: 0-status.py
Description: A module that contains code for solving log parsing problem
             in python.
Date Created: May 12, 2023
Author: Gizachew Bayness
"""
from sys import stdin


def status_printer(total_size, status):
    """A method to print the status with the format given"""
    print('File size: {}'.format(total_size))
    for code, count in sorted(status.items()):
        if count > 0:
            print('{}: {:d}'.format(code, count))


def main():
    """Main method"""
    status_codes = {'200': 0, '301': 0, '400': 0,
                    '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total = 0
    count = 1
    try:
        for line in stdin:
            splited = line.split()
            code = splited[-2]
            if code in status_codes.keys():
                status_codes[code] = status_codes[code] + 1
            try:
                total += int(splited[-1])
            except Exception:
                pass
            if count % 10 == 0 or count == 1:
                status_printer(total_size=total, status=status_codes)
            count += 1
    except KeyboardInterrupt:
        status_printer(total, status_codes)
        raise


if __name__ == '__main__':
    main()
