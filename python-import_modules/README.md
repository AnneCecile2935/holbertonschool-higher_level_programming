# Python Import Modules Project

This project is designed to give you an introduction to Python's module system and how to handle basic operations, dynamic imports, and command-line arguments. Through a series of tasks, you'll become familiar with how to organize your code into reusable modules, how to import and use functions across files, and how to handle command-line arguments in Python scripts.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

### General
- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Resources

### Read or Watch:
- **Modules** (Understanding Python modules)
- **Command line arguments** (How to interact with the system via the command line)
- **Pycodestyle – Style Guide for Python Code** (Learn about PEP 8 standards for writing clean, readable Python code)

### man or help:
- `python3` (The Python interpreter's manual pages)

## Requirements

### General
- **Allowed editors**: vi, vim, emacs
- All your files will be interpreted/compiled on **Ubuntu 22.04 LTS** using Python 3 (version 3.10.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A **README.md** file, at the root of the project folder, is mandatory
- Your code should follow the **pycodestyle** (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

| Task Number | Task Description | File Name | Example Output |
|-------------|------------------|-----------|----------------|
| 0 | Import a simple function from a simple file | `0-add.py` | `1 + 2 = 3` |
| 1 | My first toolbox! Write a program that imports functions from `calculator_1.py`, does some maths, and prints the result. | `1-calculation.py` | `10 + 5 = 15`<br>`10 - 5 = 5`<br>`10 * 5 = 50`<br>`10 / 5 = 2` |
| 2 | How to make a script dynamic! Write a program that prints the number of arguments and the list of its arguments. | `2-args.py` | `0 arguments.`<br>`1 argument:`<br>`1: Hello`<br>`6 arguments:`<br>`1: Hello`<br>`2: Welcome`<br>... |
| 3 | Infinite addition. Write a program that prints the result of adding all arguments. | `3-infinite_add.py` | `0`<br>`89`<br>`-162` |
| 4 | Who are you? Write a program that prints all the names defined by the compiled module `hidden_4.pyc`. | `4-hidden_discovery.py` | `my_secret_santa`<br>`print_hidden`<br>`print_school` |
| 5 | Everything can be imported. Write a program that imports the variable `a` from `variable_load_5.py` and prints its value. | `5-variable_load.py` | `98` |
| 6 | Build my own calculator! Write a program that imports all functions from `calculator_1.py` and handles basic operations (addition, subtraction, multiplication, division). | `100-my_calculator.py` | `Usage: ./100-my_calculator.py <a> <operator> <b>`<br>`3 + 5 = 8`<br>`Unknown operator. Available operators: +, -, * and /` |
| 7 | Easy print. Write a program that prints `#pythoniscool` followed by a new line. You are not allowed to use `print`, `eval`, `open`, or `sys`. | `101-easy_print.py` | `#pythoniscool` |
| 8 | ByteCode -> Python #3. Write a Python function `magic_calculation(a, b)` that replicates a specific Python bytecode sequence. | `102-magic_calculation.py` | **N/A** (Tested with bytecode) |
| 9 | Fast alphabet. Write a Python program that prints the alphabet in uppercase without using loops, conditional statements, `str.join()`, string literals, or system calls. | `103-fast_alphabet.py` | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` |

## Usage

- Clone the repository:
  ```bash
  git clone https://github.com/yourusername/python-import_modules.git
  cd python-import_modules

