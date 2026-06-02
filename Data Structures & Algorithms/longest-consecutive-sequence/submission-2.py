class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setMap = set(nums)
        maxL = 0
        L = 0
        for num in nums:
            if (num - 1) not in setMap:
                L = 1
                while (num + L) in setMap:
                    L += 1
                maxL = max(maxL,L)
        return maxL 

