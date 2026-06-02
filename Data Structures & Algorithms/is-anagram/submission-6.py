class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(t) < len(s):
            return False
        
        d_s = {}
        d_t = {}

        for char in s:
            if char in d_s:
                d_s[char] += 1
            else:
                d_s[char] = 0
        
        for char1 in t:
            if char1 in d_t:
                d_t[char1] += 1
            else:
                d_t[char1] = 0
        
        for char in d_s:
            if char not in d_t or d_s[char] != d_t[char]:
                return False

        return True






           