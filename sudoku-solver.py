"""Below is the program to solve a valid 3x3 Sudoku board - Baord presented as 2D list where each element of list reprsents a row"""

def check_Validity(board, row, col, num):
    #to check if the number is present in row
    for i in range(9):
        if board[row][i] == num:
            return False
    #to check if the number exists in the column    
    for i in range(9):
        if board[j][col] == num:
            return False
    #below variables are declared to check the exitence of number in 3x3 square    
    r = row - row % 3
    c = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i+r][j+c] == num:
                return False
    return True