#!/usr/bin/python3
"""Read a file and print its content to the standard output."""
import sys


def print_status():
    """Prints the status of the request every 10 lines."""
    counter = 0
    size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 2:
                continue

            try:
                size += int(parts[-1])
                code = parts[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except (ValueError, IndexError):
                continue

            counter += 1
            if counter == 10:
                print("File size: {}".format(size))
                for key in sorted(status_codes):
                    if status_codes[key]:
                        print("{}: {}".format(key, status_codes[key]))
                counter = 0

    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(size))
        for key in sorted(status_codes):
            if status_codes[key]:
                print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    print_status()
