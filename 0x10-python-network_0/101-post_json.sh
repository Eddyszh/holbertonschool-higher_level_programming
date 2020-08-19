#!/bin/bash
# sends a JSON POST request to a URL, and displays the body
curl -sX POST -H "Content-type: application/json" $1 -d @$2
