class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = {}

        for c in s1:
            c1[c] = 1 + c1.get(c,0)

        need = len(c1)

        for i in range(len(s2)): #here we are trying to start a window
            c2 = {} #build the window rightward 
            current = 0
            for j in range(i,len(s2)): #start the window at point until you get a match
                c2[s2[j]] = 1 + c2.get(s2[j],0)
                
                #if we found that the freq of char at j in s2 is more than in s1, wrong break
                if c1.get(s2[j],0) < c2.get(s2[j]):
                    break
                if c1.get(s2[j],0) == c2.get(s2[j]):
                    current += 1
                
                if current == need:
                    return True
        return False

