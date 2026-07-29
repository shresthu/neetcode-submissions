class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def dfs(openN,closeN):
            #base case
            if openN == closeN == n:
                result.append("".join(stack))
                return
            
            if openN < n: #since we need to start and add an open
                stack.append("(")
                dfs(openN + 1,closeN)
                stack.pop() #remove the open parathesis and build
            
            if closeN < openN:
                stack.append(")")
                dfs(openN,closeN+1)
                stack.pop()
            
        dfs(0,0)
        return result
