#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    param = {'search': argv[1]}
    req = requests.get(url, params=param)

    matching_ppl = req.json()
    print("Number of results: {}".format(matching_ppl.get('count')))
    for person in matching_ppl.get('results'):
        print(person.get('name'))
