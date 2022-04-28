# Recursion_examples

Repository contains recursion examples in Python

BoggleWordSolver.py solves 4 x 4 boggle boards (finding lists of valid words)

It uses a recursively built Trie data structure to turn the words in the dictionary-yawl.txt file into markov chains. It then searches this Trie structure, buildling strings that can be found in the structure from letter chains on the boggle board.

Sudoku 4x4 solves 4 x 4 sudoku board.

It uses lists of dictionaries to store the cell: contents by rows, columns and sub-squares, searching each for existing numbers and subtracting existing numbers from the set of available numbers (1,2,3,4). It then seraches recursively for each next legal number, storing each step of the search in a data structure.