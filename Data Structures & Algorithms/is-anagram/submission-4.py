class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ds = {}
        dt = {}

        for char in t:
            dt[char] = 1 + dt.get(char,0)
        
        for c in s:
            ds[c] = 1 + ds.get(c,0)

        print(ds)
        print(dt)
        for i in ds:
            print(i)
            if(i not in dt or ds[i] != dt[i]):
                return False
        
        return True
            



