#!/usr/bin/python3

from urllib.request import urlopen
import json

with urlopen("https://covidtracking.com/data/api") as response:
    sour = response.read()
    new = sour.decode('utf-8')
print(type(new))

#data = json.loads(new)

#print(json.dumps(new, indent=2))
