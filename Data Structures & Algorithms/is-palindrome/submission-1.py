class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()

        news = ""
        for char in s:
            if(char.isalnum()):
                news += char
        
        #news is the new string to be used
        news = news.lower()
        print(news)

        l,r = 0,len(news) - 1

        while(l<=r):
            if(news[l] != news[r]):
                return False
            l += 1
            r -= 1
        
        return True