class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #here we need the max at top so process the stones, so we have max heap
        stones = [-w for w in stones]

        heapq.heapify(stones) #now we converted it into heap
        #this stores negative values and the smallest value, negative version is the largest value

        while len(stones) > 1: #we want the last stone if remaining so it will be at most 1
            first = heapq.heappop(stones) #this will be the max element of the heap
            second = heapq.heappop(stones) #this will be the second max element of the heap

            #if they are unequal
            if second > first: #since they are negative values this will be in postive terms (if -largest < -second)
                heapq.heappush(stones,first-second) #first - second means eg (-8) - (-7) we want negative value
            
            #now we they are equal then we dont need to do anything

        #now that we have processed all the numbers, we just return the first value 

        #if there is no stone so we need to return 0, so saftey check
        stones.append(0)
        return -stones[0] #since we have max heap and we have done with negative numbers of the actual numbers