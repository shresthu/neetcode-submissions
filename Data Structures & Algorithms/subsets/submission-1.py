class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []

        def dfs(index):
            #we essentially need to be recorsive process

            #base case
            if index >= len(nums):
                result.append(tmp[:])
                return

            #choosing to add the number 
            tmp.append(nums[index])
            dfs(index + 1)

            #choosing to NOT add the number
            tmp.pop()
            dfs(index + 1)
        
        dfs(0)
    
        return result