class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []
        nums = sorted(nums)

        def dfs(index):
            if index >= len(nums):
                result.append(tmp[:])
                return 
            
            #include the number
            tmp.append(nums[index])
            dfs(index + 1)

            #not include
            tmp.pop()
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
                
            dfs(index + 1)

        dfs(0)
        return result