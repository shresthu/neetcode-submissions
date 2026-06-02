class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for num in nums:
            d[num] = 1 + d.get(num,0)
            if d[num] > 1:
                return True
        return False