#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
   and then save them to a file:
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_new = "add_item.json"

try:
    new_content = load_from_json_file(file_new)
except:
    new_content = []

for i in sys.argv[1:]:
    new_content.append(i)
save_to_json_file(new_content, file_new)
