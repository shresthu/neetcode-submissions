class Solution:
    def ispali(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l + 1, r - 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        tmp = []

        def dfs(i):
            if i >= len(s):
                result.append(tmp[:])
                return 
            
            for j in range(i,len(s)):
                if self.ispali(s,i,j):
                    tmp.append(s[i:j+1])
                    dfs(j+1)
                    tmp.pop()
        dfs(0)
        return result

