class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while(l <= r):
            m = (l+r) // 2

            if(nums[m] == target):
                return m
            elif(nums[m]>=nums[l]): #we are in the left section
                if(nums[l] > target):
                    l = m + 1
                elif(target > nums[m]):
                    l = m + 1
                else:
                    r = m - 1
            else: #we are in right section
                if(nums[r] < target) or (target < nums[m]):
                    r = m - 1
                else:
                    l = m + 1
        return -1
                
