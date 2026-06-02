class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for i in s:
            map_s[i] = 1 + map_s.get(i,0)
        for j in t:
            map_t[j] = 1 + map_t.get(j,0)

        if(len(s) != len(t)):
            return False

        for char in map_s:
            if(char not in map_t or map_s[char] != map_t[char]):
                return False
        
        return True





