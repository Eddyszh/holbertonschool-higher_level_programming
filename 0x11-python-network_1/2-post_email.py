#!/usr/bin/python3
"""sends a POST request with the email as a parameter,
    and displays the body of the response
    """


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        head = response.read()
    print(head.decode(encoding="utf-8"))
