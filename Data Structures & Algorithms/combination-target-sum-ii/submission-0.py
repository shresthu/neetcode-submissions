class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        tmp = []
        candidates = sorted(candidates)

        def dfs(index,csum):
            if csum == target:
                result.append(tmp[:])
                return

            if index >= len(candidates) or csum > target:
                return
                
        
            #lets include the number
            tmp.append(candidates[index])
            dfs(index+1,csum+candidates[index])

            #dont include the number
            tmp.pop()
            while index + 1 < len(candidates) and candidates[index+1] == candidates[index]:
                index += 1

            dfs(index+1,csum)


        dfs(0,0)

        return result