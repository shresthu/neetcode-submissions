class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""

        for st in strs:
            s += str(len(st)) + "#" + st

        print(s)
        return s


    def decode(self, s: str) -> List[str]:
        #now we have to decode the string. So we have given
        # s = 5#Hello5#World
        
        result = []

        #lets build out the strings
        i = 0

        while i < len(s):
            #second pointer to get the length of the word sequence
            j = i

            while (s[j] != "#"):
                j += 1
            
            length = int(s[i:j])

            word = s[j+1 : j + 1 + length]
            print(word)

            result.append(word)

            i = j + 1 + length
        
        print(result)

        return result


























