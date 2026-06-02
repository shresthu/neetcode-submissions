class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string = string + str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        index = 0
        lst = []

        while index < len(s):
            j = index
            while(s[j] != "#"):
                j += 1
            length = int(s[index:j])
            index = j+1
            word = s[index:index+length]
            lst.append(word)
            index = index + length
        return lst

            
