class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #we are going to use min heap becuase to track of the heap sized k and then just return the first element
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        #now that we have a heap and we want to maintain the size to be of k
        while len(self.minHeap) > k: #check the length of minheap
            heapq.heappop(self.minHeap) #remove the smallest number until we have size of k

    def add(self, val: int) -> int:
        #now to add the nnumber to the heap
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
