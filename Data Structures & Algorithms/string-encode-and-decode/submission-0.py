class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            # Step 1: Find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # from i to j (not including '#')
            
            # Step 2: Extract the word of `length` chars
            word = s[j+1 : j+1+length]
            l.append(word)
            
            # Step 3: Move i forward to the next encoded word
            i = j + 1 + length
        return l

            
