#!/bin/bash
# takes in a URL, sends a request, and displays the size of the body
curl -so /dev/null $1 -w '%{size_download}\n'
