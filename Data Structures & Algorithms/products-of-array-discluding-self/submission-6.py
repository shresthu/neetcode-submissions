class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rlist = [1]*(len(nums))

        #going from left to right to find the prefix values 
        prefix = 1
        for i in range(len(nums)):
            rlist[i] = prefix
            prefix *= nums[i]
        
        #going from right to left to find the postvalues
        postfix  = 1
        for j in range(len(nums)-1,-1,-1):
            rlist[j] = rlist[j]*postfix
            postfix *= nums[j]

        return rlist


