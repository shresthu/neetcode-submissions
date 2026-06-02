# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(not root):
            return root
        
        if(root.val == p) or (root.val == q):
            return root
        
        if(p.val < root.val and q.val < root.val):
            #check the left side tree
            print("inside the left side",root.val)
            return self.lowestCommonAncestor(root.left,p,q)

        if(p.val > root.val and q.val > root.val):
            #check the left side tree
            print("inside the right side",root.val)
            return self.lowestCommonAncestor(root.right,p,q)
        
        #check left and right side
        return root











