#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
stored in a JSON file named 'add_item.json'.

Usage:
    ./script.py item1 item2 item3

- If 'add_item.json' exists, the script loads the existing list,
  appends new items, and saves it back.
- If the file doesn't exist, it creates it and saves the list with
the new items.
- Uses 'save_to_json_file' and 'load_from_json_file' functions from
  separate modules.

No exception handling is done for file permissions or JSON errors.
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Main function to load the list from 'add_item.json',
    append command-line arguments to the list,
    and save the updated list back to the JSON file.

    Reads arguments passed to the script excluding the script name itself,
    handles the case where the file does not exist by initializing
    an empty list.
    """
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
