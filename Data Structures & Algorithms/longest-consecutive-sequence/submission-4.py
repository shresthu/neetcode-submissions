class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        s = set(nums)

        for num in nums:
            #start of the sequence
            if num - 1 not in s:
                length = 1
                while (num + length) in s:
                    length += 1
                maxLength = max(maxLength,length)
        return maxLength

