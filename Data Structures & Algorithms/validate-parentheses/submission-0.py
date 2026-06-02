class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {
                        ")":"(",
                        "]":"[",    
                        "}":"{"
                    }
        
        for c in s:
            if c in bracketMap.values():
                stack.append(c)
            elif c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0



