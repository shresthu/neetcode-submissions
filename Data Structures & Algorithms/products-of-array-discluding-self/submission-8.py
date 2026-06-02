class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) 
        
        #prefix_result
        prefix = 1
        for i,num in enumerate(nums):
            result[i] = prefix
            prefix *= num
        
        postfix = 1
        for index in range(len(result)-1,-1,-1):
            result[index] *= postfix
            postfix = postfix*nums[index]

        return result