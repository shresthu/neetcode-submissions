# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #here we are going to use BFS approach since we want the last of each level

        q = deque()
        result = []

        if not root:
            return result
        
        q.append(root)

        while q: #go thorugh the queue until its empty
            rightSide = None #pointer to the last node in the current level
            qLen = len(q) #maintain the length of the q at this level

            for i in range(qLen): #go to the end of current level
                node = q.popleft()
                if node: #if node is non NULL
                    rightSide = node #this pointer keeps updating until the last node of current level
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSide:
                result.append(rightSide.val)
        
        return result

