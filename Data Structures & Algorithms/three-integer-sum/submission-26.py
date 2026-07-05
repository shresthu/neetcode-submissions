class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i in range(len(nums)-2): #we do -2 since we need 3 value to add up to 0
            
            if i > 0 and nums[i] == nums[i-1]: #since we do not want same triplets, we ignore all starting points with same number
                continue
            
            first = nums[i]

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = first + nums[l] + nums[r]

                if threeSum < 0: #if less than zero we need to increase the value by moving l
                    l += 1

                elif threeSum > 0:
                    r -= 1
                
                else:
                    #we found a match where sum == 0
                    result.append([first,nums[l],nums[r]])

                    l += 1
                    r -= 1

                    #since we dont want repeated second and third values we will skip it

                    while l < r and nums[l] == nums[l-1]: #since same l values we skip the sond value
                        l += 1

                    while l < r and nums[r] == nums[r+1]: #since same r values we skip the third value
                        r -= 1
        
        return result




