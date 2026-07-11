# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we have to build the BST from these 2 lists
        while preorder or inorder:
            root = TreeNode(preorder[0])
            mid = inorder.index(root.val) #we find the index of the root and hence we will divide it into 2 left is left sub tree and right is right sub tree

            #now we have to build the tree left side and right side
            #left side is going to be in preorder from [1:mid + 1] and inorder from [:mid]
            #right side is going to be in prorder from [mid + 1: ]  and in order from [mid+1: ]


            root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

            return root        

