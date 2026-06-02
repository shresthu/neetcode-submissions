class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        #first we need to build the dict to keep track of 
        #what difference exists so 7 - 3 = 4 , is 4 in dict ?
        #if yes return the current index and index of where we found
        #diff to be 4 
        for index, num in enumerate(nums):
            diff = target - num
            if (diff in d):
                return [d[diff],index]
            else:
                d[num] = index
        
        return []