class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            result = []
            l = 0
            q = collections.deque()

            for r in range(len(nums)):
                while q and nums[q[-1]] < nums[r]:
                    q.pop()
                q.append(r)
                # print(q)

                if q[0] < l:
                    q.popleft()
                
                if (r - l + 1) == k:
                    # print("inside the window " + str(l) + " " + str(r))
                    result.append(nums[q[0]])
                    # print(f"result = {result}")
                    l += 1
                
                # print("l = " + str(l) + " r =  " + str(r))
                # print("end loop ------------")
            
            return result
