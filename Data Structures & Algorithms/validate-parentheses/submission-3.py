class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        } #map to hold the values

        stack = [] #hold the opening bracket

        for bracket in s: #go through the string s and take each bracket
            if(bracket in bmap.values()): #if it is an opening bracket
                stack.append(bracket) #add to the stack where we hold the opening brackets
            elif(bracket in bmap): #if it is an closing bracket
                if(stack and stack[-1] == bmap[bracket]): #if the stack is not empty 
                #and stack last element is same as value of closing bracket in map
                    stack.pop()
                else: #if the bracket dont match in map
                    return False
        return len(stack) == 0



