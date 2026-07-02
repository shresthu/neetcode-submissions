class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #here we are going to have 2 pass approach
        #pre and post 

        result = [1] * len(nums)

        #pre
        pre = 1

        for index in range(len(nums)):
            result[index] = pre
            pre = pre*nums[index]

        print(result)

        post = 1
        for index in range(len(nums)-1,-1,-1):
            result[index] = result[index] * post
            post = post * nums[index]
        
        return result