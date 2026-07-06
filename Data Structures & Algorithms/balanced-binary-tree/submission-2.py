# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #here we need to essnetially check whther at the current node, if the left and right height
        #is balanceed ... which means it is either 0 or 1

        #this function tells us that hey at current node am i balanced or not
        def dfs(curr):

            if not curr: #means if we are at the end node of the tree
                return [True,0] #the height at that point is 0 since we are on last node and it is true 

            left = dfs(curr.left)
            right = dfs(curr.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced,1 + max(left[1],right[1])]

        result = dfs(root)

        return result[0]





        