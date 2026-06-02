class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i in range(len(nums)-2):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            first = nums[i]
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                threesum = first + nums[left] + nums[right]

                if threesum == 0:
                    result.append([first,nums[left],nums[right]])

                    while (left < right) and nums[left] == nums[left+1]:
                        left += 1
                    
                    while (left < right) and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif (threesum < 0):
                    left += 1
                else:
                    right -= 1                    

        return result 
                
