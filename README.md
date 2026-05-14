# Scientific Computing with Python

This repository contains Python programs completed while learning scientific computing concepts. The programs cover basic Python syntax, algorithms, data structures, numerical computing, pandas, NumPy, and simple utility applications.

## Programs Included

### `arithmeticformatter.py`
Formats arithmetic problems vertically so they are easier to read. It supports addition and subtraction problems, checks for input errors, aligns numbers correctly, and can optionally display the answers.

### `bisection.py`
Uses the bisection method to approximate the square root of a number. The program repeatedly narrows the search range until it finds a close estimate based on a given tolerance.

### `caseconverter.py`
Converts a PascalCase or camelCase string into snake_case. This program demonstrates string manipulation, list comprehension, and checking uppercase letters.

### `datapandas.py`
Creates a small pandas DataFrame using study hours, sleep hours, and pass/fail results. It prints the first rows of the dataset and basic statistical information using pandas methods.

### `expensetracker.py`
A simple command-line expense tracker. It allows the user to add expenses, list all expenses, calculate total expenses, and filter expenses by category.

### `luhnalgorithm.py`
Implements the Luhn algorithm to verify whether a card number is valid. The program removes spaces or dashes, processes the digits, and checks if the final sum is divisible by 10.

### `mse.py`
Calculates Mean Squared Error using NumPy. It compares actual values with predicted values, finds the errors, squares them, and calculates the average squared error.

### `numpylearn1.py`
Demonstrates basic NumPy operations using arrays, matrices, and dot products. It also prints the shape of the data and the result of multiplying the data matrix by weights.

### `passwordgenerator.py`
Generates a secure random password using Python's `secrets`, `string`, and `re` modules. The password can include required numbers, special characters, uppercase letters, and lowercase letters.

### `shortpathalgorithm.py`
Implements a shortest path algorithm using a weighted graph. It calculates the shortest distance and path between nodes, such as finding the shortest path from node `A` to node `F`.

### `vigenerecaesar.py`
Implements a Vigenere cipher for encryption and decryption. It uses a custom key to shift letters and can decode an encrypted message back into readable text.

### `recursion.py`
Implements a recursive solution to solve the mathematical puzzle known as the Tower of Hanoi. The puzzle consists of three rods and a number of disks of different diameters. The goal of this puzzle is moving the disks from the first rod to the third rod, following specific rules that restrict placing a larger disk on top of a smaller one.

### `mergesortalgorithm.py`
The Merge Sort Algorithm is a sorting algorithm based on the divide and conquer principle.
Here, we interact with data structures by sorting a list of random numbers using the Merge Sort Algorithm.

### `timecalculator.py`
A simple time calculator without using any python libraries that takes the input in AM or PM and add duration and days to find out the result.

### `sudokusolver.py`
In this project, we simply use classes and objects to build a Sudoku grid and to solve a Sudoku puzzle.

### `binarysearchtree.py`
A Binary Search Tree (BST) is an common data structure where data is sorted hierarchically.In this project,we construct our own BST and perform an in-order traversal while using key operations like insertion, search, and deletion.

### `budgetapp.py`
This project is a Budget App where we create budget categories such as Food, Clothing, and Entertainment. Each category will store its deposits, withdrawals, and transfers inside a ledger list. Later, we will also create a spending chart that compares how much was spent from each category. The project is mainly testing our understanding of classes, methods, lists, dictionaries, string formatting, and functions in Python.

### `vectorspace.py`
This program demonstrates how vector objects can be created and manipulated using object-oriented programming in Python. The program defines 2D and 3D vector classes, supports inheritance, and implements common vector operations such as representation, equality comparison, norm calculation, scalar multiplication, dot product, and cross product for 3D vectors. Overall, the program shows how mathematical vector behavior can be modeled using Python classes and special methods.

### `equationsolver.py`
In this project, we'll discover how to implement an interface in Python while building a simple equation solver program.

## How to Run

Make sure Python is installed, then run any file from the terminal:

```bash
python filename.py
```

Example:

```bash
python expensetracker.py
```

Some files require additional libraries:

```bash
pip install numpy pandas
```

## Purpose

The purpose of this repository is to practice core Python programming skills and scientific computing concepts. These programs show basic problem solving, algorithm design, data handling, and numerical computation in Python.
