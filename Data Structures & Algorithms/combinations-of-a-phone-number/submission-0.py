class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        

        def dfs(i,cs):
            if len(cs) == len(digits):
                result.append(cs)
                return 
            
            for c in digitToChar[digits[i]]:
                #here we are taking the first digit of digits and building from there
                dfs(i+1,cs+c)
            
        if digits:
            dfs(0,"")

        return result
