class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #storing the freq of the word we see
        result = 0 #max length we have to return

        l = 0 #hold the left pointer
        for r in range(len(s)): #right pointer moves until the end and we build the substring
            count[s[r]] = 1 + count.get(s[r],0) #build the count map 

            if (r-l+1) - max(count.values()) > k: #check if the window  - freq of most common is more than k
                count[s[l]] -= 1
                l += 1 #shift the left pointer until you you meet the condition
            
            result = max(result,r-l+1) #the max window we can get, r is the max it goes and l updates 
        
        return result


