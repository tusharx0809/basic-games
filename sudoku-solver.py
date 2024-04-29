"""Below is the program to solve a Valid 3x3 Sudoku board - Baord presented as 2D list where each element of list reprsents a row and empty blocks are reprsented by a '0'"""

#function to check if the number is not already present in row, column or 3x3 inside box
def check_Validity(sudoku_board, row, col, num):
    
    #to check if the number is present in row
    for i in range(9):
        if sudoku_board[row][i] == num:
            return False
        
    #to check if the number exists in the column    
    for i in range(9):
        if sudoku_board[j][col] == num:
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
                        