class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we are going to use the way of frequency mapping and bucket sort
        hmap = {}
        buckets = [[] for i in range(len(nums) + 1)]
        r_list = []
        for num in nums:
            hmap[num] = 1 + hmap.get(num,0)
        for num,cnt in hmap.items():
            buckets[cnt].append(num)

        for bucket in range(len(buckets)-1,-1,-1):
            for num in buckets[bucket]:
                r_list.append(num)
                if(len(r_list) == k):
                    return r_list

            



            
        