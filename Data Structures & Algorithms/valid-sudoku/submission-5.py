class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #so we are going to solve this using hasmap of sets
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        BOXES = defaultdict(set) #this will save key -> val where key is (row // 3, col // 3)

        for r in range(9): #we loop through the each row
            for c in range(9): #we loop through each col 
                if board[r][c] == ".":
                    continue
                elif board[r][c] in ROWS[r]: #if the row has seen this number before, not valid
                    return False
                elif board[r][c] in COLS[c]: #if the col has seen this number before, not valid
                    return False
                elif board[r][c] in BOXES[(r // 3 , c // 3 )]: #if this particular 3x3 box has seen this number before
                    return False
                else:
                    ROWS[r].add(board[r][c])
                    COLS[c].add(board[r][c])
                    BOXES[(r // 3, c //3)].add(board[r][c])

        return True