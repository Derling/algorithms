'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

class Solution(object):
    def isvalidsudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns_checked = []
        for i in range(len(board)):
            if not self.__check_row(board, i):
                return False
            for j in range(len(board)):
                if not i % 3 and not j % 3: 
                        if not self.__check_square(board, i, j):
                            return False
                elif board[i][j].isdigit() and j not in columns_checked:
                    if not self.__check_column(board, j):
                        return False
                    columns_checked.append(j)
        return True
                
    def __check_row(self, board, row):
        row_nums = []
        for i in range(len(board)):
            if board[row][i] in row_nums:
                return False
            elif board[row][i].isdigit():
                row_nums.append(board[row][i])
        return True
    
    def __check_column(self, board, col):
        col_nums = []
        for i in range(len(board)):
            if board[i][col] in col_nums:
                return False
            elif board[i][col].isdigit():
                col_nums.append(board[i][col])
        return True
    
    def __check_square(self, board, row, col):
        square_nums = []
        for i in range(row, row + 3):
            for j in range(col , col + 3):
                if board[i][j] in square_nums:
                    return False
                elif board[i][j].isdigit():
                    square_nums.append(board[i][j])
        return True


if __name__ == '__main__':
    '''
    . 8 7 6 5 4 3 2 1
    2 . . . . . . . .
    3 . . . . . . . .
    4 . . . . . . . .
    5 . . . . . . . .
    6 . . . . . . . .
    7 . . . . . . . .
    8 . . . . . . . .
    9 . . . . . . . .
    '''
    board = [
        [".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]
    ]
    s = Solution()
    print(s.isvalidsudoku(board))
