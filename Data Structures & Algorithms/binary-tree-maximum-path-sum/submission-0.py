# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf") #this is going to be our max value, initialized to be -ve inf

        #now we need to find the max path sum of a node
        def dfs(node):
            #we are going to depth first search since we want to go from bottom to up
            if not node:
                return 0 #since no node there we reach base case which is zero

            #now lets calculate the left sum and right sum
            left = dfs(node.left)
            right = dfs(node.right)

            left = max(0,left) #since we can have negative nodes, we need to check and make sure and return 0 if there is negative values
            right = max(0,right) #described as above
            
            #now that we found the max sum of left side and max sum of right side
            self.maxSum = max(self.maxSum,(left+right+node.val)) #the max sum at current is node is left + right + node

            #now what we have to return at the current node is that we see either the left side or right side of current node
            return max(left,right) + node.val
        
        dfs(root)
        return self.maxSum