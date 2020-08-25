#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
