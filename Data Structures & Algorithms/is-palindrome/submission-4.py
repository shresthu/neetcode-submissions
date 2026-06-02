class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""

        for char in s:
            if char.isalnum():
                news += char
        news = news.lower()

        l = 0 
        r = len(news) - 1

        while(l<=r):
            if(news[l] != news[r]):
                return False
            l += 1
            r -= 1
        return True