class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        #create a sorted from last to first
        pairs = sorted(zip(position,speed), reverse = True)

        for p,s in pairs:
            time = (target-p)/s
            stack.append(time)

            #if we have a scene where the time at the top is less than at 2nd then pop
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)



