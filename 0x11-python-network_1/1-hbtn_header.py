#!/usr/bin/python3
"""displays the value of the X-Request-Id
    variable found in the header of the response
    """


if __name__ == "__main__":
    import urllib.request
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))
