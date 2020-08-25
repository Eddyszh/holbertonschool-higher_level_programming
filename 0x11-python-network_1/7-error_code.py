#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
    displays the body of the response
    """


if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    code = r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
