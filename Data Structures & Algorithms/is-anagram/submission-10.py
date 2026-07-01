class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for char in s:
            s_map[char] = s_map.get(char,0) + 1
        
        for char in t:
            t_map[char] = t_map.get(char,0) + 1


        print(s_map)
        print(t_map)

        for c in s_map:
            if c not in t_map or s_map[c] != t_map[c]:
                return False

        return True







           