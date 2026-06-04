class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #building the intiuition, rows and columns check is easy
        #just build a dict of sets, since we do not want duplicates
        #now coming to each square, from row and column we can find it like so
        #row // 3 , col // 3

        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        #here the columns and rows go from 0 -> 8 
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r // 3,c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r // 3,c // 3)].add(board[r][c])

        return True