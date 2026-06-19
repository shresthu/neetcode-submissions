class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #firstly we will try to find the extact row where the target could be
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0 
        bot = ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break #break since target is probably in the mid one
            
        if not ( top <= bot):
            return False
        
        #target is proabably in the mid one

        l = 0
        r = COLS - 1
        row = (top + bot) // 2

        while l <= r:
            m = (l + r) // 2
            
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        
        return False
            