class TimeMap:

    def __init__(self):
        self.store = {} #here we store the key and value pair where value is list of lists of value and tmpstmp

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store.get(key).append([value,timestamp])
                

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        #lets get all the values that we meed based on key
        values = self.store.get(key,[])

        #now lets look through the list of values since it is increasing order we use binary search
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l+r) // 2

            #if the middle value in the list of values of the key is less than or equal to time stamp
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid- 1
        return result 



