class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for st in strs:
            encoded_string += str(len(st)) + "#" +  st
    
        print(encoded_string)
        return encoded_string

    # #5Hello#5World
    def decode(self, s: str) -> List[str]:
        return_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length

            sub_s = s[i:j]
            return_list.append(sub_s)

            i = j

        return return_list


