class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        #prefix
        prefix = 1
        for index,num in enumerate(nums):
            result[index] = prefix
            prefix *= num
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


