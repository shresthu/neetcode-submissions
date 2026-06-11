class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        l = 0 
        result = 0

        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r],0)

            #condition if the window is invalid then update left pointer
            if (r-l+1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1

            result = max(result,r-l+1)
        return result