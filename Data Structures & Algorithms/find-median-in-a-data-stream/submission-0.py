class MedianFinder:

    def __init__(self):
        #so we are going to use two different heaps to keep track. one small and one large
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        #here we will add numbers to our data strctures which is small(maxheap) and large(minheap)
        #small is maxheap since we want it to have max element(-ve version) at top
        #large is minheap since we want it to have min element(+ve usual element) at top
        if self.large and num >= self.large[0]:
            #belongs to larger heap
            heapq.heappush(self.large,num) #add to the larger one
        else:
            heapq.heappush(self.small,-1*num) #add to the smaller one

        #now that we added the number we need to keep a track of sizes of the 2
        #since we want to keep the size difference at max of 1 so that
        #the mediam element is either the max of the smaller or min of the larger

        if len(self.large) > len(self.small) + 1: #if the larger heap length is more than 2 of length of small
            element_popped = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*element_popped)
        elif len(self.small) > len(self.large) + 1:
            element_popped = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,element_popped)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0]) / 2     






