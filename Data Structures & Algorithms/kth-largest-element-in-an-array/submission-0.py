class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #brute force is 
        # nums.sort()
        # return nums[-k]  

        #optimised would be max heap
        nums = [-num for num in nums]
        heapq.heapify(nums)

        result = 0
        while k > 0:
            result = heapq.heappop(nums)
            print(result)
            k -= 1
        return -result