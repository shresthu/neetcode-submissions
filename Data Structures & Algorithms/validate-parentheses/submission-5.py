class Solution:
    def isValid(self, s: str) -> bool:
        mapBrackets = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }

        stack = []
        
        for b in s:
            if b in mapBrackets:
                if stack and mapBrackets[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return len(stack) == 0