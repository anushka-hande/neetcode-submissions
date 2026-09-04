class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        while True:
            prev = s
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            if s == prev:
                break

        return s == ""