class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #okay so we are solving it using stack
        stack = [] #store the pair of height and index
        maxA = 0

        for i,height in enumerate(heights):
            start = i #starting index
            #if stack is not empty and the heigh we are at is more than the height at top of stack(previous heihgt)
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                maxA = max(maxA, h * (i - j) ) #area is equal to the smaller height we at into index we at - index of the higher rectangle on left
                start = j #and we essentially save the start of the index going leftwards 
            stack.append((height,start))

            #now the ones which are left behind essentially the ones which extend in both directions
        while stack:
            h,j = stack.pop()
            w = len(heights) - j
            maxA = max(maxA, h*w)
                
        return maxA

