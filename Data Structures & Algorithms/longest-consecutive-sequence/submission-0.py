class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = set(nums)
        longest = 0
        
        for num in nums:
            length = 0
            if(num-1) not in new_list:
                while(num+length in new_list):
                    length += 1
            longest = max(length,longest)

        return longest

            


            
        