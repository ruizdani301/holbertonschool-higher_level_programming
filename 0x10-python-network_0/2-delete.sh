#!/bin/bash
#Write a Bash script that sends
#a DELETE request to the URL passed as the first argument
curl -Xs 'DELETE' '$1'
