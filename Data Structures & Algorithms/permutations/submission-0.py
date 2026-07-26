class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []
        s = set()

        def dfs(tmp, used):
            if len(tmp) == len(nums):
                result.append(tmp[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                tmp.append(nums[i])
                used.add(i)
                dfs(tmp, used)
                tmp.pop()
                used.remove(i)
        
        dfs([],s)

        return result