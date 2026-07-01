class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #starting the pointers at 0
        slow = 0
        fast = 0

        #we are given that there is a cycle and we just have to find it
        while True:
            #now we need to move the slow pointer where it "jums" to value stored at 0
            slow = nums[slow]
            #now we update fast to jump to 2 times the value of first one
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #now we essentially have the point where the cycle end
        #we need a slow pointer starting at 0 where each of the slow pointers move 1 step at
        # a time
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow