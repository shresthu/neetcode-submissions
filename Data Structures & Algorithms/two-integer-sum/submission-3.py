class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #to solve we consider, index and difference
        #say we start at index 0 and difference target - index val
        # we store that and if that value is equal to any next element
        #we found the sol

        diff_dict = {}

        for index,num in enumerate(nums):
            diff = target - num #check the diff

            if num in diff_dict:
                return [diff_dict[num],index]

            diff_dict[diff] = index #store pair of diff and index

        return []