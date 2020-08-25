#!/usr/bin/python3
"""takes your Github credentials and uses the Github API to display your id
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2])).json()
    if 'id' in r:
        print(r['id'])
    else:
        print(None)
