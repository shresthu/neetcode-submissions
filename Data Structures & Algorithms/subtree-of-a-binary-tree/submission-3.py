# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: #if the subTree is empty, offcourse it will be a subtree of another
            return True
        
        if not root:   #if there is no s but t, doesnt makes sense that anything can be subtree of empty tryy
            return False

        #this checks if the trees are same
        def isSameTree(p,q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        #now we have to check if the trees are exact match

        if isSameTree(root,subRoot):  #if the root and subroot are exactly same offcourse we are same tree
            return True


        #but we need to check both sides right

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)








