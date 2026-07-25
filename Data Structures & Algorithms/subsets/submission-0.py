class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #we need to provide all the possible subsets of the nums list.
        #this also includes []
        result = []
        tmp = []
        
        def backtrack(index):
            if index >= len(nums):
                result.append(tmp[:])
                return 

            #here we shall include the number
            tmp.append(nums[index])
            backtrack(index+1) #go onto the next numbers

            #here we shall NOT include the number
            tmp.pop()
            backtrack(index+1) #go onto the next numbers
        
        backtrack(0)
        return result 