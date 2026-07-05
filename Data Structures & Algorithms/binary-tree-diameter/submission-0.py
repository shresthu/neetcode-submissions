# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #this returns the height of the tree
        def dfs(curr):
            if not curr: #check if we reach the end of the tree i.e. bottom
                return 0
            
            left = dfs(curr.left) #go through the left side and find the last element
            right = dfs(curr.right) #go through the right side and find the last element

            self.res = max(self.res, left + right) #return the max height at that point
            return 1 + max(left,right) #diameter is essentially 1 + max height
        
        dfs(root)
        return self.res






