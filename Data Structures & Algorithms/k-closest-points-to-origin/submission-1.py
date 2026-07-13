
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create tuples with point and distance such as 
        # (distance,[point])

        result = []

        for index,point in enumerate(points):
            result.append((point[0]**2 + point[1]**2,point))

        heapq.heapify(result)

        res = []
        while k > 0:
            element = heapq.heappop(result)
            res.append(element[1])
            k -= 1
        
        return res

