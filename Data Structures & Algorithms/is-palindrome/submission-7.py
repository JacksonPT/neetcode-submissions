class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for x in s:
            if x.isalnum():
                newStr = newStr + x
        
        flippedS = newStr[::-1]
        flippedS = flippedS.lower()
        newStr = newStr.lower()
        
        if newStr == flippedS:
            return True
        return False