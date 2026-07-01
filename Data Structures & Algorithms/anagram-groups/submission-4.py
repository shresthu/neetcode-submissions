class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hmap = {}

        for word in strs:
            #we are going to take the word and generate a sorted word out of it and save as key
            key = "".join(sorted(word))

            if key in hmap:
                hmap[key].append(word)
            else:
                hmap[key] = [word]
        
        return list(hmap.values())