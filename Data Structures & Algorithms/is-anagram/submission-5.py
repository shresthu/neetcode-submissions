class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ds = {}
        dt = {}

        for char in s:
            ds[char] = 1 + ds.get(char,0)
        
        for ch in t:
            dt[ch] = 1 + dt.get(ch,0)

        for c in ds:
            if c not in dt or ds[c] != dt[c]:
                return False
        return True