# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #to solve this we are going to need a sub function which will
        #tell us if we are balanced at that point and go up

        def dfs(curr):
            if not curr:
                return [True,0]

            #now that we have done with the base case, lets check
            left = dfs(curr.left) #check the left subtree
            right = dfs(curr.right) #check the right subtree

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced,1 + max(left[1],right[1])]
        
        result = dfs(root)

        return result[0]





        