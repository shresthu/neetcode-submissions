class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        tmp = []

        def dfs(index, curr_sum):
            if curr_sum == target:
                result.append(tmp[:])
                return
            if curr_sum > target or index >= len(nums):
                return

            # include nums[index], allow reuse
            tmp.append(nums[index])
            dfs(index, curr_sum + nums[index])
            tmp.pop()

            # exclude nums[index], move on
            dfs(index + 1, curr_sum)

        dfs(0, 0)
        return result