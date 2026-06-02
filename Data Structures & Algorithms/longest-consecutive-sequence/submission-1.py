class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxV = 0
        for num in nums:
            if(num-1 not in s):
                length = 1
                while(num+length in s):
                    length += 1
                maxV = max(maxV,length)
        return maxV
                

