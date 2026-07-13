class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        hmap = {}
        l = 0

        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r],0)
            #now we have a hmap to keep track of the element which was added

            #if window size - max value of element > k, means we do not have enough elements to replace, window break
            if (r-l+1) - max(hmap.values()) > k: 
                hmap[s[l]] -= 1 #remove the first element from the window
                l += 1 #move the left pointer to shrink the window
            
            maxLen = max(maxLen,r-l+1)
        
        return maxLen
