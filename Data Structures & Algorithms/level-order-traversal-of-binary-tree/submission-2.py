# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            qLen = len(q) #get the exisitng lenght of queue
            level = [] #this will hold the current level nodes

            for i in range(qLen): #iterate through the length of q
                node = q.popleft() #pop the element
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        
        return result
            