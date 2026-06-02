class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index,value in enumerate(nums):
            complement = target - value 
            if(complement in hashMap):
                return [hashMap[complement],index]
            hashMap[value] = index
            
        return []