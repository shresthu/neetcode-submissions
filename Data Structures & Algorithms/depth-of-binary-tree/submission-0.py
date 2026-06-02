# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if(not root):
    #         return 0

    #     return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
        
        stack = [[root,1]] #at least there is 1 depth(the root)
        res = 1
        while(stack): #go through the stack
            node,depth = stack.pop() #check what is the node and where we are

            if node: #if the node is existing
                res = max(res,depth) #find the max depth
                stack.append([node.left,depth + 1]) #add the left child 
                stack.append([node.right,depth + 1]) #add the right child

        return res










