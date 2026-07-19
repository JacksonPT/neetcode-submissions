class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1

        
            
        while L < R:

            while not s[L].isalnum():
                L += 1
                if L == len(s)-1:
                    break
            while not s[R].isalnum() and R != 0:
                R -= 1
                if R == 0:
                    break
            
            if L > R:
                break
            if s[L].upper() != s[R].upper():
                return False
            
            L += 1
            R -= 1
            
        
        return True