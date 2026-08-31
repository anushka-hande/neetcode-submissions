class Solution:
    def isPalindrome(self, s: str) -> bool:
        nStr = ''
        for c in s:
            if c.isalnum():
                nStr += c.lower()
        return nStr == nStr[::-1]