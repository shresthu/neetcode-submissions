class Solution:
    def trap(self, height: List[int]) -> int:
        #water stored at a point is equal to the minimum of left or right - height of column at i
        res = 0
        l,r = 0,len(height)-1
        Lmax,Rmax = height[l],height[r] #currently the lmax and rmax is height at 0 and end of list

        while l < r: #we close in from both sides
            if Lmax < Rmax: #if the left side max value is less than right side of max, we are going to base it on left side is going to be the minimum value 
                l += 1
                Lmax = max(Lmax,height[l])
                res += Lmax - height[l]
            else: #we are going to use right max value Rmax is less than or equal to Lmax
                r -= 1
                Rmax = max(Rmax,height[r])
                res += Rmax - height[r]
        return res

        
        
        