class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        tmp = []

        def dfs(index,curr_sum):

            #base case if the sum of tmp is equal to target, store it
            if curr_sum == target:
                result.append(tmp[:])
                return             
            
            if index >= len(nums) or curr_sum > target:
                return 
            
            #include the first number
            tmp.append(nums[index])
            dfs(index,curr_sum + nums[index])
            tmp.pop()

            dfs(index+1, curr_sum)
        
        dfs(0,0)

        return result