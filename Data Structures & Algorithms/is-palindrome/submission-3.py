class Solution:
    def isPalindrome(self, s: str) -> bool:
        striped = s.strip()
        reverse = striped[::-1]
        replaced = reverse.replace("?","").replace(".","").replace("!","").replace(" ","").replace(",", "").replace("'","").replace(":","")
        lower = replaced.lower()
        if lower == s.lower().strip().replace("?","").replace(".","").replace("!","").replace(" ", "").replace(",", "").replace("'","").replace(":",""):
            print(s)
            return True
        return False

