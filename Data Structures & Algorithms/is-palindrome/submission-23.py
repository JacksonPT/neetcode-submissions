class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1

        
            
        while L < R:

            while not s[L].isalnum() and L != len(s)-1:
                L += 1

            while not s[R].isalnum() and R != 0:
                R -= 1
            
            if L > R:
                break
            if s[L].upper() != s[R].upper():
                return False
            
            L += 1
            R -= 1
            
        
        return True