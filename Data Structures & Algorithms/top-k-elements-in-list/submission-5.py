class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #here we are going to use bucket sort where each bucket will hold those numbers
        result = []
        buckets = [ [] for i in range(len(nums)+1) ]

        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
        
        #now lets fill the buckets

        for key,val in hmap.items():
            buckets[val].append(key)

        print(buckets)

        for i in range(len(buckets)-1,-1,-1):
            b = buckets[i]
            for num in b:
                result.append(num)
            
            if len(result) == k:
                return result
        
        return []
