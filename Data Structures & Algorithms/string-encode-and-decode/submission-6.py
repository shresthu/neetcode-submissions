class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            l = len(word)
            s += str(l) + "#" + word
        
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        rlist = []
        #given s as 4#neet4#code
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            rlist.append(s[i:i+length])
            i = i+length

        return rlist
