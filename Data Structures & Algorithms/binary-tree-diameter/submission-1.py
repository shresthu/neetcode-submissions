# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #this function return the height but we do not necessarily need it, we need the diameter
        #which is usually 1 more than the height on left side and height on right side
        def dfs(curr):
            #base case, if the height is zero -> return 0
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            self.res = max(self.res,left+right) #we want to maximize this 

            return 1 + max(left,right)

        dfs(root)

        return self.res





