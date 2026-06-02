class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxF = 0
        maxLen = 0
        left = 0

        for right in range(len(s)):
            d[s[right]] += 1
            maxF = max(maxF,d[s[right]])
            if (right - left + 1) - maxF > k:
                d[s[left]] -= 1
                left += 1
            maxLen = max(maxLen,right - left + 1)
        
        return maxLen
