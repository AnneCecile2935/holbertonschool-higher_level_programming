#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text (new_string) into a file after every line
    that contains a specific search string (search_string).

    Args:
        filename (str): The path to the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching line.

    Returns:
        None

    Note:
        - The function overwrites the original file with the updated content.
        - It uses the 'with' statement for file operations.
        - It does not handle exceptions related to file permissions or missing
        files.
    """
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        f.seek(0)
        for line in lines:
            f.write(line)
