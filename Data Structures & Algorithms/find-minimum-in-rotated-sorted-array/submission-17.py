class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we need to find the min element in sorted array.
        #so we are needing to essentially use binary search based on the fact that where the mid value compare
        #to the left most element since it is sorted and rotated.
        result = nums[0]
        l = 0
        r = len(nums) - 1

        #search through the list using points
        while l <= r:
            #check if the array is in ascending order
            if nums[l] < nums[r]:
                result = min(result,nums[l])
                return result

            #not in ascending so we need to find the middle element
            mid = (l+r)//2
            result = min(result,nums[mid])

            #check if the middle value is greater than equal to left most element
            if nums[mid] >= nums[l]:
                #if this is true means that we have a sorted portion on left side which is increasing
                #so we need to search right side
                l = mid + 1
            else:
                #if the middle value is < left most value then we need to search left side
                r = mid - 1


        return result
