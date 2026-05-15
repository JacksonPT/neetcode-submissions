class Solution:
    def isPalindrome(self, s: str) -> bool:
        R = len(s)-1
        L = 0
        while L<R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if (s[L].lower() != s[R].lower()):
                return False
            L += 1
            R -= 1
        return True
