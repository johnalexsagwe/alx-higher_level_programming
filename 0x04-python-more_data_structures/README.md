# ALX Higher Level Programming - Technical Write-up

## Introduction
This technical write-up outlines the requirements and tasks for the project in the "0x04-python-more_data_structures" directory. The project consists of writing Python functions to perform various operations on data structures, such as lists and dictionaries. These functions are required to meet specific coding standards and constraints, and the project's structure and requirements are detailed below.

## Project Requirements
### General Requirements
1. **Editors:** The project must be developed using one of the following text editors: vi, vim, or emacs.
2. **Platform:** All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
3. **Newline:** All code files must end with a newline.
4. **Shebang:** The first line of all code files must begin with `#!/usr/bin/python3`.
5. **README.md:** A README.md file must be present at the root of the project folder, providing an overview of the project and explaining how to use the code.
6. **pycodestyle:** The code should adhere to the pycodestyle style guide (version 2.8.*).
7. **Executable Files:** All code files must be executable.
8. **File Length:** The length of the code files will be tested using the `wc` command.

### Task Requirements
#### Task 0: Squared Simple
- **Function:** `square_matrix_simple(matrix=[]):`
- Accepts a 2-dimensional matrix (list of lists) as input.
- Returns a new matrix of the same size where each value is the square of the corresponding value in the input matrix.
- The initial matrix should not be modified.
- No external modules should be imported, and regular loops or map functions are allowed for implementation.

#### Task 1: Search and Replace
- **Function:** `search_replace(my_list, search, replace)`
- Takes an initial list (`my_list`), a search element (`search`), and a replacement element (`replace`) as input.
- Replaces all occurrences of the search element with the replacement element in a new list and returns the new list.
- No external modules should be imported.

#### Task 2: Unique Addition
- **Function:** `uniq_add(my_list=[])`
- Accepts a list of integers as input and returns the sum of unique integers in the list.
- No external modules should be imported.

#### Task 3: Present in Both
- **Function:** `common_elements(set_1, set_2)`
- Takes two sets as input and returns a set containing common elements found in both input sets.
- No external modules should be imported.

#### Task 4: Only Differents
- **Function:** `only_diff_elements(set_1, set_2)`
- Accepts two sets as input and returns a set containing elements that are present in only one of the input sets.
- No external modules should be imported.

#### Task 5: Number of Keys
- **Function:** `number_keys(a_dictionary)`
- Receives a dictionary as input and returns the number of keys in the dictionary.
- No external modules should be imported.

#### Task 6: Print Sorted Dictionary
- **Function:** `print_sorted_dictionary(a_dictionary)`
- Takes a dictionary with string keys as input and prints its keys sorted in alphabetical order.
- The function should not sort keys within nested dictionaries.
- No external modules should be imported.

#### Task 7: Update Dictionary
- **Function:** `update_dictionary(a_dictionary, key, value)`
- Accepts a dictionary, a key, and a value as input.
- Replaces or adds a key/value pair in the dictionary.
- No external modules should be imported.

#### Task 8: Simple Delete by Key
- **Function:** `simple_delete(a_dictionary, key="")`
- Accepts a dictionary and a key (default value is an empty string).
- Deletes the specified key from the dictionary if it exists.
- No external modules should be imported.

#### Task 9: Multiply by 2
- **Function:** `multiply_by_2(a_dictionary)`
- Takes a dictionary with integer values as input and returns a new dictionary where all values are multiplied by 2.
- No external modules should be imported.

#### Task 10: Best Score
- **Function:** `best_score(a_dictionary)`
- Receives a dictionary with integer values as input and returns the key with the highest integer value.
- If no score is found, it returns `None`.
- No external modules should be imported.

#### Task 11: Multiply by Using Map
- **Function:** `multiply_list_map(my_list=[], number=0)`
- Takes a list of integers and a number as input.
- Returns a new list where each value is the result of multiplying the corresponding value in the input list by the given number.
- Uses the `map` function for implementation.
- No loops or external modules should be used.

#### Task 12: Roman to Integer
- **Function:** `roman_to_int(roman_string)`
- Accepts a Roman numeral string as input and returns the corresponding integer.
- Handles Roman numerals from 1 to 3999.
- If the input is not a valid string or `None`, it returns 0.
- No external modules should be imported.

#### Task 13: Weighted Average
- **Function:** `weight_average(my_list=[])`
- Takes a list of tuples, where each tuple contains a score and a weight.
- Returns the weighted average of the scores in the list.
- If the list is empty, it returns 0.
- No external modules should be imported.

#### Task 14: Squared by Using Map
- **Function:** `square_matrix_map(matrix=[])`
- Accepts a 2-dimensional matrix (list of lists) as input.
- Returns a new matrix of the same size where each value is the square of the corresponding value in the input matrix.
- The initial matrix should not be modified.
- Uses the `map` function for implementation.
- No loops or external modules should be used.

#### Task 15: Delete by Value
- **Function:** `complex_delete(a_dictionary, value)`
- Takes a dictionary and a value as input.
- Deletes all keys having the specified value from the dictionary.
- No external modules should be imported.

## Conclusion
The "0x04-python-more_data_structures" project involves developing various Python functions to manipulate data structures while adhering to specific coding standards and constraints. Each function performs a specific operation, such as square calculations, element replacement, key deletion, and more. The project is a valuable opportunity to practice Python programming, data structure manipulation, and code optimization.
