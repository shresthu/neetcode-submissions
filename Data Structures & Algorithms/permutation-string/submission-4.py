class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we want to find s1 in s2
        if not s2 and s1:
            return False
        if not s1:
            return False
        
        s1map = Counter(s1)
        have = len(s1map)
        
        for i in range(len(s2)):
            s2map = {} #grow the map if we have a potential map
            seen = 0 #increase only if match or start over

            for j in range(i,len(s2)):
                s2map[s2[j]] = 1 + s2map.get(s2[j],0)

                #if it doesnt exist in s1map, break .. didnt find a match start over
                if s1map.get(s2[j],0) < s2map[s2[j]]:
                    break
                
                #if it matches the values, great got a match !
                if s1map.get(s2[j],0) == s2map.get(s2[j]):
                    seen += 1
                
                if have == seen: #match the number of unique requirmenets and their number
                    return True
        
        return False

