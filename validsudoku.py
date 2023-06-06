from typing import List # import this because LeetCode.com uses the capital List vs lower list
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #define row, column and square
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c] in columns[c] 
                    or board[r][c] in squares[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                # add value to data structure
        return True
    
    
    



#valid
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# not valid 2 6s in first column
board2 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,["6",".",".",".","8",".",".","7","9"]]


sol = Solution()
print(sol.isValidSudoku(board))
print(sol.isValidSudoku(board2))

