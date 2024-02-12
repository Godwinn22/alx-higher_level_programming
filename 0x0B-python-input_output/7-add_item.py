#!/usr/bin/python3
"""Defines a script that adds all arguments to a
Python list, and then save them to a file"""
import os.path
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
file_name = 'add_item.json'
lists = []
if os.path.exists(file_name):
    lists = load_from_json_file(file_name)

for i in range(1, len(sys.argv)):
    lists.append(sys.argv[i])

save_to_json_file(lists, file_name)
