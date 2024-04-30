"""Below is the program to solve a Valid 3x3 Sudoku board - Baord presented as 2D list where each element of list reprsents a row and empty blocks are reprsented by a '0'"""

import random

#This functions generates a random valid sudoku puzzle
def generate_sudoku_board(): 
    base = 3
    side = base * base
    nums = random.sample(range(1, side + 1), side) #generates a list of random numbers from 1 to 9
    board = [] #initialize an empty board

    for r in range(side):
        row = []
        for c in range(side):
            idx = (base * (r % base) + r // base + c) % side
            #above formula is used to fill up each 3x3 inside board
            num = nums[idx]
            row.append(num)
        board.append(row)
    return board

#function to check if the number is not already present in row, column or 3x3 inside box
def check_Validity(sudoku_board, row, col, num):
    #to check if the number is present in row
    for i in range(9):
        if sudoku_board[row][i] == num:
            return False
        
    #to check if the number exists in the column    
    for i in range(9):
        if sudoku_board[i][col] == num:
            return False
        
    #below variables are declared to check the exitence of number in 3x3 square    
    r = row - row % 3
    c = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku_board[i+r][j+c] == num:
                return False
    return True

#function to solve 3x3 sudoku board
def solve_sudoku_board(sudoku_board):
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                for num in range(1,10):
                    #At this step, we will check the validity of the number, if true then we assign block the number num.
                    if check_Validity(sudoku_board, i, j, num):
                        sudoku_board[i][j] = num
                        if solve_sudoku_board(sudoku_board):#check if the sudoku is solved and return True, else keep keep checking for each block until function return True
                            return True
                        else:
                            sudoku_board[i][j] = 0
                return False
    return True

sudoku_board =  generate_sudoku_board()
for i in range(len(sudoku_board)):
    print(sudoku_board[i])


#call solve_sudoku_function with passing the value as above board
solve_sudoku_board(sudoku_board)
#print the solved sudoku puzzle
input("Press Enter to solve above puzzle!")
for i in range(len(sudoku_board)):
    print(sudoku_board[i])