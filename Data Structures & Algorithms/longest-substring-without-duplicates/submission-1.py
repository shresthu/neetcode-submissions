class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0
        for r in range(len(s)): #keeps track of each char as we move
            while(s[r] in charset): #check if the char we see is in the set
                charset.remove(s[l]) #if found remove the first element from the set
                l += 1 #move the l pointer to plus 1
            charset.add(s[r])
            res=max(res,r-l+1) #compare the exisiting value to window size as l only moves when duplicates
        return res 
                
                

