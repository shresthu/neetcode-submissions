class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            A,B = nums2,nums1
        else:
            A,B = nums1,nums2
        
        #here we have achieve the smaller array in A

        total = len(A) + len(B)
        half = total // 2

        #we are going to binary search in the smaller Array since we are fixating on finding the pivot
        lo,hi = 0,len(A)

        while lo <= hi:
            i = (lo + hi) // 2 #here we are finding the point where we find the mid of array A
            j = half - i #this is essentially the other half so i + j == half of length

            #now that we have access to the middle element, we are going to find the condition
            Aleft = A[i-1] if i > 0 else float("-infinity")   #this is the left element of the middle point of array A
            Aright = A[i]  if i < len(A) else float("infinity") #this is the mid point where we divide the array A
            Bleft = B[j-1] if j > 0 else float("-infinity") #this is the left point of middle of B
            Bright = B[j]  if j < len(B) else float("infinity") #this is the middle or the last point of section of array B

            #now that we the elements surrounding the median point
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1

                


