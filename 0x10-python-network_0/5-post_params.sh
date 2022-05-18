#!/bin/bash
#script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX POST -H "email:test@gmail.com" "$1"
curl -sX POST -H "subject:I will always be here for PLD" "$1"