class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        setmap = set()
        maxL = 0

        for r in range(len(s)):
            while s[r] in setmap:
                    setmap.remove(s[l])
                    l += 1                
            setmap.add(s[r])
            maxL = max(maxL,r-l+1)
        return maxL

                

