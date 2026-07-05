class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) #here we create a set since lookup will be O(1)
        result = 0

        #we need to find the max length of consecutive numbers
        #we find the start of the window when we see if the number - 1 isnt there in s
        for i in range(len(nums)):
            if (nums[i] - 1) not in s:
                #we found the start of the sequence
                length = 1
                #while the next number is present in the s, keep increasing length
                while (nums[i] + length) in s:
                    length += 1
                result = max(result,length)
        
        return result
                
