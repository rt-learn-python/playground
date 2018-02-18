#!/usr/bin/env python3

import requests
import json

url = 'https://s3-ap-southeast-1.amazonaws.com/roycetest/sample.json'
response = json.loads(requests.get(url).text)
print(response)

print (response["name"])
