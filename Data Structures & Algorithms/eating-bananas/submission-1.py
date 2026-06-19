class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #here we have the need to decide on the min number of bananas to be eaten per hour.
        #which has to be at max the max value in the piles so max(piles)

        l = 1
        r = max(piles)
        result = max(piles)

        #loop thorugh each value of possible k values [l:r]
        while l <= r:
            mid = (l+r) // 2

            #lets check how many hours it takes when we take the mid value in k values
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / mid)
            
            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid - 1
                result = min(result,mid)

        return result

            
