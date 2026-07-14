import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxs = defaultdict(list)

        for r in range(0,9):
            for c in range (0,9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])

                cord1 = math.floor(r/3)
                cord2 = math.floor(c/3)
                if board[r][c] in boxs[cord1,cord2]:
                    return False
                boxs[cord1,cord2].append(board[r][c])
        return True
                


            

        

