class Solution:
    def isPalindrome(self, s: str) -> bool:
        strHold = ''
        for x in s:
            if x.isalnum():
                strHold += x.lower()
        if strHold == strHold[::-1]:
            return True
        return False

