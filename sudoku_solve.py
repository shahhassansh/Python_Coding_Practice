## The below code solves the sudoku.
##
## Input:
##
## [[".",".",".","7",".",".","3",".","1"],
# ["3",".",".","9",".",".",".",".","."],
# [".","4",".","3","1",".","2",".","."],
# [".","6",".","4",".",".","5",".","."],
# [".",".",".",".",".",".",".",".","."],
# [".",".","1",".",".","8",".","4","."],
# [".",".","6",".","2","1",".","5","."],
# [".",".",".",".",".","9",".",".","8"],
# ["8",".","5",".",".","4",".",".","."]]
##
## Output:
##
## True

def sudoku_solve(board):
    def can_find():
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == '.':
                    return i,j
        return -1,-1

    def sub_start(x):
        if x<3:
            return 0
        elif x>=3 and x<6:
            return 3
        else:
            return 6
    def can_place(i,j,num):
        for c in range(0,len(board[0])):
            if board[i][c] == num:
                return 0
        for r in range(0,len(board)):
            if board[r][j] == num:
                return 0
        st_x = sub_start(i)
        st_y = sub_start(j)
        for x in range(st_x,st_x+3):
            for y in range(st_y,st_y+3):
                if board[x][y] == num:
                    return 0
        return 1
        

        
    def solve():
        r, c = can_find()

        if r == -1 and c == -1:
            return True

        for num in  range(1, 10):
            num = str(num)
            if can_place(r, c, num):
                board[r][c] = num
                if solve():
                    return True
                board[r][c] = '.'
        return False
    
    if not board:
        return
    if solve() == True:
        return True
    else:
        return False

board = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
print(sudoku_solve(board))
