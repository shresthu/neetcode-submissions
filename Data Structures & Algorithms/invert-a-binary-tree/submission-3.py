# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #check if root is null
        if not root:
            return None
        
        #now we are going to invert the roots
        temp = root.left
        root.left = root.right #here swap the values
        root.right = temp 

        #so now we have swapped the children

        #now lets call this on left side
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root