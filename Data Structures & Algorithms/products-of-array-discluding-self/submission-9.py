class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1 for i in range(len(nums))]

         #left side mul
        pre = 1
        for i in range(len(nums)):
            prod[i] = pre
            pre = pre * nums[i]

         #right side mul
        post = 1
        for i in range(len(nums)-1,-1,-1):
            prod[i] = prod[i] * post
            post = post * nums[i]
        return prod