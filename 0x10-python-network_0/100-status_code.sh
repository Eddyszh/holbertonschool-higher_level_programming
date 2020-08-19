#!/bin/bash
# sends a request to a URL, and displays only the status code
curl -sw '%{http_code}' $1
