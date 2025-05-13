# Project: Python - More Data Structures: Set, Dictionary

## Description

This project focuses on understanding and applying Python data structures, specifically sets and dictionaries. You'll write various functions to manipulate these structures and learn useful Python methods and techniques.

---

## Task Table

| Task Number | Function Name               | Description                                                                 | Prototype                                                     | Example/Execution                                                                                               |
|-------------|-----------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 0           | `square_matrix_simple`       | Computes the square value of all integers of a matrix.                      | `def square_matrix_simple(matrix=[])`                         | **Input**: `matrix = [[1, 2, 3], [4, 5, 6]]`<br>**Output**: `[[1, 4, 9], [16, 25, 36]]`                        |
| 1           | `search_replace`             | Replaces all occurrences of an element by another in a new list.            | `def search_replace(my_list, search, replace)`                | **Input**: `my_list = [1, 2, 3, 4]`, `search = 2`, `replace = 99`<br>**Output**: `[1, 99, 3, 4]`               |
| 2           | `uniq_add`                   | Adds all unique integers in a list only once.                               | `def uniq_add(my_list=[])`                                     | **Input**: `my_list = [1, 2, 2, 3]`<br>**Output**: `6`                                                      |
| 3           | `common_elements`            | Returns a set of common elements in two sets.                               | `def common_elements(set_1, set_2)`                           | **Input**: `set_1 = {1, 2, 3}`, `set_2 = {2, 3, 4}`<br>**Output**: `{2, 3}`                                   |
| 4           | `only_diff_elements`         | Returns a set of elements that appear in only one of the two sets.          | `def only_diff_elements(set_1, set_2)`                        | **Input**: `set_1 = {1, 2, 3}`, `set_2 = {2, 3, 4}`<br>**Output**: `{1, 4}`                                   |
| 5           | `number_keys`                | Returns the number of keys in a dictionary.                                | `def number_keys(a_dictionary)`                               | **Input**: `a_dictionary = {'a': 1, 'b': 2}`<br>**Output**: `2`                                               |
| 6           | `print_sorted_dictionary`    | Prints a dictionary sorted by keys in alphabetical order.                   | `def print_sorted_dictionary(a_dictionary)`                   | **Input**: `a_dictionary = {'b': 3, 'a': 1, 'c': 2}`<br>**Output**: `{'a': 1, 'b': 3, 'c': 2}`                |
| 7           | `update_dictionary`          | Replaces or adds a key/value in a dictionary.                               | `def update_dictionary(a_dictionary, key, value)`             | **Input**: `a_dictionary = {'a': 1}`, `key = 'b'`, `value = 2`<br>**Output**: `{'a': 1, 'b': 2}`               |
| 8           | `simple_delete`              | Deletes a key in a dictionary.                                              | `def simple_delete(a_dictionary, key="")`                     | **Input**: `a_dictionary = {'a': 1, 'b': 2}`, `key = 'a'`<br>**Output**: `{'b': 2}`                           |
| 9           | `multiply_by_2`              | Returns a new dictionary with all values multiplied by 2.                   | `def multiply_by_2(a_dictionary)`                              | **Input**: `a_dictionary = {'a': 1, 'b': 2}`<br>**Output**: `{'a': 2, 'b': 4}`                               |
| 10          | `best_score`                 | Returns a key with the biggest integer value in a dictionary.               | `def best_score(a_dictionary)`                                 | **Input**: `a_dictionary = {'a': 10, 'b': 20}`<br>**Output**: `'b'`                                          |
| 11          | `multiply_list_map`          | Returns a new list with all values multiplied by a number using `map`.       | `def multiply_list_map(my_list=[], number=0)`                  | **Input**: `my_list = [1, 2, 3]`, `number = 2`<br>**Output**: `[2, 4, 6]`                                    |
| 12          | `roman_to_int`               | Converts a Roman numeral to an integer.                                     | `def roman_to_int(roman_string)`                                | **Input**: `roman_string = 'X'`<br>**Output**: `10`                                                           |
| 13          | `weight_average`             | Returns the weighted average of a list of tuples `<score>, <weight>`.       | `def weight_average(my_list=[])`                                | **Input**: `my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]`<br>**Output**: `2.80`                                |
| 14          | `square_matrix_map`          | Computes the square value of all integers in a matrix using `map`.          | `def square_matrix_map(matrix=[])`                              | **Input**: `matrix = [[1, 2], [3, 4]]`<br>**Output**: `[[1, 4], [9, 16]]`                                    |
| 15          | `complex_delete`             | Deletes keys with a specific value in a dictionary.                        | `def complex_delete(a_dictionary, value)`                      | **Input**: `a_dictionary = {'a': 'x', 'b': 'y'}`, `value = 'x'`<br>**Output**: `{'b': 'y'}`                   |

---

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Learning Objectives

By the end of this project, you should be able to:

- Understand why Python programming is awesome
- Learn how to use sets and dictionaries, and understand their key methods
- Use lambda functions, and understand `map`, `filter`, and `reduce`
- Understand when to use sets versus lists or dictionaries

---


