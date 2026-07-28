class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #we need to find the permutations of all possible values in nums
        #essentially we need a wak to track each digit at each position at max 1
        result = []
        tmp = []
        s = set() #this will keep track of the state of visited idxs

        def dfs(tmp,seen):
            if len(tmp) == len(nums):
                result.append(tmp[:])
                return
            
            for i in range(len(nums)):
                if i in seen:
                    continue
                tmp.append(nums[i])
                seen.add(i)
                dfs(tmp,seen)
                tmp.pop()
                seen.remove(i)

        dfs([],s)

        return result