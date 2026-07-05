class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while(l < r):
            #we are going to use binary search here and going to close the window based
            #on if we are higher or lower than the target value
            mid = (l+r) // 2
            print(f"mid {mid}")
            print(f"l {l}")
            print(f"right {r}")

            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
                
            elif numbers[l] + numbers[r] < target:
                l += 1
            
            elif numbers[l] + numbers[r] > target:
                r -= 1
            
        return []