# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #the goal here is to find the diameter, so to do that, we need to essentially 
        #check where the largest diameter is, which means what is the max distance
        #from the left node to the right node

        #we will keep the largest diameter and try to maximize it using following viariable
        self.res = 0

        #through this function we will check the height and try to maximize the self.res
        def dfs(curr):
            if not curr: #if no node, we reach end and height is essentially zero
                return 0

            left = dfs(curr.left) #check and return the height on the left side
            right = dfs(curr.right) #check and return the height on the right side

            #now that we have the height lets try to maximize the diameter at current node
            self.res = max(self.res,left + right) #we see at current node what is max vs left height + right height

            return 1 + max(left,right) #this return to the function that hey we got the height of current node with 1 + max height on left or right side

        dfs(root)

        return self.res



