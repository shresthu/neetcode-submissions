class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        l = 0
        maxl = 0
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r],0)

            if (r -l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            
            maxl = max(maxl,r-l+1)
        return maxl


