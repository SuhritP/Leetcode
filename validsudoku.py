class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or
                    board[r][c] in square[r //3 , c //3]):
                    return False
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[r//3, c//3].add(board[r][c])
        return True 
        

# basic sudoku rules are you can't have a repeating number in the row, col or square of that number, start by initializing
# the row col and square, with default value as a set, next iterate thorugh the board and first check if its a '.' which
# is an empty square and continue, next check if the row[r] contains that number or col[c] or the square[r//3,c//3]
# we check that square as we want to index the squares as a 3 by 3 as that is easier compared to just trying to access
# the 9x9 elements and check if it contains that number, if it doesn't then we add it to that row, col and that square
# the T.C is O(1) as the grid is 9x9 and insertions and membership checks take O(1) time and the S.C is also O(1) as 
# the number of items being stored is bounded and fixed 