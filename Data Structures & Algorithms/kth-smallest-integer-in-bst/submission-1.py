# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = [] #this stores the node values as we go, we always pop the smallest elements as we go through the list
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            #here we have reached the smallest element from the list

            curr = stack.pop()
            k -= 1 #since we popped one elements, we need to decrease k since we popped the smallest element

            if k == 0: #if we reach the kth smallest element, we just return the current popped element
                return curr.val 
            
            curr = curr.right #keep building from left to right and the right node keeps getting added to it
            

