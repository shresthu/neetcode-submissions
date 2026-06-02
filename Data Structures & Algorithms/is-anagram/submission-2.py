class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        if (len(s) == len(t)):
            for i in s:
                if(i not in d_s):
                    d_s[i] = 1
                d_s[i] += 1

            for j in t:
                if(j not in d_t):
                    d_t[j] = 1
                d_t[j] += 1

            for k in d_s:
                if(k not in d_t or d_s[k] != d_t[k]):
                    return False
            return True
        return False
