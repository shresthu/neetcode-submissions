class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        
        l = 0
        mapT = {}
        window = {}

        for c in t:
            mapT[c] = 1 + mapT.get(c,0)

        result = [-1,-1]
        resultlen = float("infinity")
        have = 0
        need = len(mapT)

        for r in range(len(s)):
            #add the first word from list in the window
            char = s[r]
            window[char] = 1 + window.get(char,0)

            #we see that we have met an exact match of the word freq
            if char in mapT and mapT[char] == window[char]:
                have += 1

            #we have the successful window
            while have == need:
                #we see a success window so store the result:
                if (r- l + 1) < resultlen:
                    result = [l,r]
                    resultlen = r-l+1
                
                #remove from the left
                window[s[l]] -= 1

                #check if we break the window
                if s[l] in mapT and mapT[s[l]] > window[s[l]]:
                    have -= 1
                
                l+= 1
        
        l,r = result
        return s[l:r+1] if resultlen != float("infinity") else ""


















        
        