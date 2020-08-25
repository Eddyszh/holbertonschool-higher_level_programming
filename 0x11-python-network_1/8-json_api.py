#!/usr/bin/python3
"""takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
    """


if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, data={'q': q}).json()
        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
