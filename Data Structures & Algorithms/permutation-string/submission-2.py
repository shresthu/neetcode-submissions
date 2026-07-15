class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we want to find s1 in s2
        if not s2 and s1:
            return False
        if not s1:
            return False
        
        s1map = Counter(s1)

        #we need to keep track of what unique numbers have and what we have seen
        have = len(s1map)

        for i in range(len(s2)):
            #we will build our s2map
            seen = 0
            s2map = {}


            for j in range(i,len(s2)):
                #start to check if we get a match from this point on
                s2map[s2[j]] = 1 + s2map.get(s2[j],0) #add first element

                #check if the element matches any in s1map else break
                if s1map.get(s2[j],0) < s2map[s2[j]]:
                    break #didnt find the start of match of s1
                
                if s1map.get(s2[j],0) == s2map.get(s2[j],0):
                    seen += 1
                
                if seen == have:
                    return True
        
        return False




