# Python - Test-Driven Development

## 📚 Description

This project focuses on the **Test-Driven Development (TDD)** approach in Python. The goal is to write unit and interactive tests before implementing functionality, reinforcing strong coding practices like documentation, input validation, and edge case handling.

---

## 🚀 Learning Objectives

- Understand the principles and benefits of Test-Driven Development
- Learn how to use `doctest` and `unittest` modules in Python
- Properly write docstrings for modules and functions
- Handle edge cases and validate user inputs effectively
- Build functions with clean, testable code

---

## 🛠️ Requirements

- Python 3.8.5
- No external imports allowed
- All code follows `pycodestyle` (v2.7.\*)
- All tests located in a `/tests` directory
- Tests run with `doctest` and `unittest`
- Each function/module is documented

---

## ✅ Task Summary

| Task # | File(s)                         | Description                                      | Test Method   |
|--------|----------------------------------|--------------------------------------------------|----------------|
| 0      | `0-add_integer.py`              | Add two integers with type checks                | `doctest`      |
| 1      | `2-matrix_divided.py`           | Divide a matrix by a number                      | `doctest`      |
| 2      | `3-say_my_name.py`              | Print a full name                                | `doctest`      |
| 3      | `4-print_square.py`             | Print a square with `#`                          | `doctest`      |
| 4      | `5-text_indentation.py`         | Format text with proper indentation              | `doctest`      |
| 5      | `6-max_integer.py`, test file   | Find max integer in list (unit test)             | `unittest`     |

---

## 📌 Usage Examples

### Add Integer:
```python
add_integer(100, 2)
# Output: 102
```
### Running Tests:

Run doctests:
python3 -m doctest ./tests/*.txt -v

Run unit tests:
python3 -m unittest tests.6-max_integer_test

### 👨‍💻 Author
Anne-Cécile Colléter
