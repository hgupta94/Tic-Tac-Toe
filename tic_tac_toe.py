# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:49:52 2019

@author: hirsh
"""


import numpy as np
import pandas as pd

# Create empty board
column_names = ['A', 'B', 'C']
row_names = [1, 2, 3]
empty_array = np.array([['*', '*', '*'], 
                        ['*', '*', '*'], 
                        ['*', '*', '*']])
board = pd.DataFrame(empty_array, columns=column_names, index=row_names)

# If player places 3 markers in a row, column, or diagonally, game is over. Otherwise, game continues
def game_result(board):
    result = 'Not over'
    if board['A'][1] == board['B'][1] == board['C'][1] != '*':
        result = 'Game over'
    elif board['A'][2] == board['B'][2] == board['C'][2] != '*':
        result = 'Game over'
    elif board['A'][3] == board['B'][3] == board['C'][3] != '*':
        result = 'Game over'
    elif board['A'][1] == board['A'][2] == board['A'][3] != '*':
        result = 'Game over'
    elif board['B'][1] == board['B'][2] == board['B'][3] != '*':
        result = 'Game over'
    elif board['C'][1] == board['C'][2] == board['C'][3] != '*':
        result = 'Game over'
    elif board['A'][1] == board['B'][2] == board['C'][3] != '*':
        result = 'Game over'
    elif board['A'][3] == board['B'][2] == board['C'][1] != '*':
        result = 'Game over'
    return(result)

# Create a function to iterate through player 1 & player 2 moves, catching any 
# errors that may appear (typo, marker already placed)
def p1_move():
    p1Marker = "X"
    while game_result(board) != 'Game over':
        p1Col = input("P1 choose a column (A, B, C): ")
        if p1Col.upper() == 'A' or p1Col.upper() == 'B' or p1Col.upper() == 'C':
            pass
        else:
            print("This is not a valid column. Please go again.")
            continue
        p1Row = input("P1 choose a row (1, 2, 3): ")
        if p1Row == '1' or p1Row == '2' or p1Row == '3':
            pass
        else:
            print("This is not a valid row. Please start over.")
            continue
        if board[p1Col.upper()][int(p1Row)] != '*':
            print("This move has been made. Please go again.")
            continue
        board[p1Col.upper()][int(p1Row)] = p1Marker
        print(board)
        if game_result(board) == 'Game over':
                print('Congratulations! P1 wins!')
                break
        break

def p2_move():
    p2Marker = "O"
    while game_result(board) != 'Game over':
        p2Col = input("P2 choose a column (A, B, C): ")
        if p2Col.upper() == 'A' or p2Col.upper() == 'B' or p2Col.upper() == 'C':
            pass
        else:
            print("This is not a valid column. Please go agian.")
            continue
        p2Row = input("P2 choose a row (1, 2, 3): ")
        if p2Row == '1' or p2Row == '2' or p2Row == '3':
            pass
        else:
            print("This is not a valid row. Please start over.")
            continue
        if board[p2Col.upper()][int(p2Row)] != '*':
            print("This move has been made. Please go again.")
            continue
        board[p2Col.upper()][int(p2Row)] = p2Marker
        print(board)
        if game_result(board) == 'Game over':
                print('Congratulations! P2 wins!')
                break
        break

# Play the game
print(board)
while game_result(board) != 'Game over':
    p1_move()
    if '*' not in board.values and game_result(board) != 'Game over':
        print('Tie game')
        break
    p2_move()
    if '*' not in board.values and game_result(board) != 'Game over':
        print('Tie game')
        break
