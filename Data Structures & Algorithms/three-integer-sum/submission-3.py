class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        lst = []

        for index in range(len(nums)-2):
            
            if(index > 0) and nums[index] == nums[index-1]:
                continue

            first = nums[index]
            left = index + 1
            right = len(nums) - 1

            while(left < right):
                Sum = first + nums[left] + nums[right]

                if(Sum < 0):
                    left += 1
                elif(Sum > 0):
                    right -= 1
                elif Sum == 0:
                    lst.append([first,nums[left],nums[right]])

                    while (left < right) and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while (left < right) and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return lst



                
