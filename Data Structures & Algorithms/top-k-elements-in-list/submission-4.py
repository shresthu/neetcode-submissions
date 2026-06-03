class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we have to create a freq bucket to hold all the values inside it
        #the values are based on the index of the value so essentially
        #what is in the 1st bucket has the freq of 1 etc.

        freq_bucket = [[] for i in range(len(nums)+1)]
        freq = {}

        #build a dict of frequency against a number
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        #now we have to append the numbers inside the freq_bucket
        for numb,count in freq.items():
            freq_bucket[count].append(numb)

        freq_number = []

        for i in range(len(freq_bucket)-1,0,-1):
            for number in freq_bucket[i]:
                if len(freq_number) == k:
                    return freq_number
                freq_number.append(number)
        


        return freq_number