class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #we need to check in the nums if the element exists
        while l <= r:
            m = (l+r) // 2

            #check if the element is found at mid
            if nums[m] == target:
                return m

            #the element needs to found in either to left or right
            #go into the left sorted portion and check 
            if nums[m] >= nums[l]:
                #if the target is more tjam middle value or target is less than left most value search right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                #otherwise search left
                else:
                    r= m - 1

            #check the right sorted portion
            else:
                #check if the target is less than middle value or target is more than right most search left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                #search right side otherwise
                else:
                    l = m + 1                
                    
        return -1
            