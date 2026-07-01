class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        #here we are going to find where the cycle is there in the nums

        while True:
            slow = nums[slow] #slow pointer would be pointing to next one
            fast = nums[nums[fast]] #it is moving/pointing 2 steps ahead

            if slow == fast:
                break

            #now we have found the slow pointer and fast pointer at the end point of cycle

        slow2 = 0

            #we start at the start to find the element which is going to be the start of cycle
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow