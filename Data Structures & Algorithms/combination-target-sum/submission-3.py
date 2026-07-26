class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #we need to find the combination of all possible values which add to target
        result = []
        tmp = []

        def dfs(index,curr_sum):
            if curr_sum == target:
                result.append(tmp[:])
                return 
            if index >= len(nums) or curr_sum > target:
                return 
            #two base cases reached and fixed

            #lets include the number to build out tmp
            tmp.append(nums[index])
            dfs(index,curr_sum + nums[index])

            #lets not include the number to our tmp
            tmp.pop()
            dfs(index+1,curr_sum)
        
        dfs(0,0)

        return result
        