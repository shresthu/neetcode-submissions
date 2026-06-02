class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string = string + str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]: #4#neet4#code4#love3#you
        lst = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            lst.append(word)
            i = i+length

        return lst

            
