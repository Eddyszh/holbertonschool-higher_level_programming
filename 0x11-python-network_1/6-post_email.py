#!/usr/bin/python3
"""sends a POST request with the email as a parameter,
    and displays the body of the response
    """


if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.post(argv[1], data={'email':argv[2]}).text
    print(r)
