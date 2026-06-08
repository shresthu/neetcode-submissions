class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        for num in nums:
            length = 0
            if(num-1) not in s:
                #start of sequence
                length += 1
                while(num+1) in s:
                    length += 1
                    num = num + 1
            longest = max(longest,length)

        return longest

