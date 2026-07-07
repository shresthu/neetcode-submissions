# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #here essentially we need to find number of good nodes which means
        #the nodes have to larger or equal to the root node

        #this function essentially processes the number of good nodes
        def dfs(node,maxVal):
            if not node:    #if the node is NULL, empty tree means no node at all so 0
                return 0
            
            #now that we have a node, how do we check if the node is good or not
            #if the node value is greater than equal to max Val then it is good node else not
            result = 1 if node.val >= maxVal else 0 
            maxVal = max(maxVal,node.val)

            #now that we checked the current node is good or not, we need to go left and right

            result += dfs(node.left,maxVal) #check the number of good nodes to the left
            result += dfs(node.right,maxVal) #check the number of good nodes to the right

            return result
        
        return dfs(root,root.val)