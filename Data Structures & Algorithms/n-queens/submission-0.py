class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()

        def dfs(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in posDiag or (row + col) in negDiag:
                    continue
                
                board[row][col] = "Q"
                cols.add(col)
                posDiag.add(row - col)
                negDiag.add(row + col)
                
                dfs(row + 1)
                
                board[row][col] = "."
                cols.remove(col)
                posDiag.remove(row - col)
                negDiag.remove(row + col)

        dfs(0)
        return result