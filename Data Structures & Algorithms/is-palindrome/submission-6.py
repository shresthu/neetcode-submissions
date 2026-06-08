class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for st in s:
            if st.isalnum():
                new_s += st.lower()
        
        l = 0
        r = len(new_s) - 1

        while (l < r):
            if new_s[l] != new_s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True