class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        lo, hi = 0, m
        
        while lo <= hi:
            i = (lo + hi) // 2      # partition point in nums1
            j = half - i            # partition point in nums2
            
            Aleft  = nums1[i-1] if i > 0 else float('-inf')
            Aright = nums1[i]   if i < m else float('inf')
            Bleft  = nums2[j-1] if j > 0 else float('-inf')
            Bright = nums2[j]   if j < n else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                # correct partition found
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                hi = i - 1   # too far right in nums1, move left
            else:
                lo = i + 1   # too far left in nums1, move right