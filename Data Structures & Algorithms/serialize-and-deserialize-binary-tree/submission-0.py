# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = []

        def dfs(node):
            if not node:
                stack.append("N")
                return 
            #now that we are done with the base case

            stack.append(str(node.val)) #if we see a node, append it to the list and move to left and right

            #check left and right 
            left = dfs(node.left)
            right = dfs(node.right)

            return stack
        
        dfs(root)
        return ",".join(stack)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #we need to decode it from preorder traversal string
        data = data.split(",")
        
        #we need a pointer to keep track of which node we are processing
        self.i = 0

        def dfs(): #here we have this function to build out the BST
            if data[self.i] == "N": #we encounter a null Node
                self.i += 1
                return 

            #so we processed the base case
            root = TreeNode(int(data[self.i])) #we create a root node at current if not "N"
            self.i += 1 #move to the next pointer

            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()

        



          



















