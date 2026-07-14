class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       #so here we essentially need to find the least TIME which is needed to process all the tasks
       #lets take [X,X,Y,Y] with n = 2
       # we essentially will take the frequency of maximum and process it.

        c = Counter(tasks) #this build a hashmap { X: 2, Y: 2}
        maxHeap = [-cnt for cnt in c.values()] #this will build the list of -ve values since we want max heap
        heapq.heapify(maxHeap) #this creates a max heap so it will be like [-2,-2] where each -2 is for X and Ys
        q = deque()
        time = 0

        while maxHeap or q: #we have more tasks to keep track of 
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # add 1 since we want to decrease and we have 0ve vals

                if cnt: #we cant really add tasks that have finished 
                    q.append([cnt,time+n]) #add to the queue the task and the time at which it will be called

            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])

        return time         



