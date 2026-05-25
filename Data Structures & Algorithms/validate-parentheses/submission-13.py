class Solution:
    def isValid(self, s: str) -> bool:
        pdict = {"}": "{", "]": "[", ")":"("}
        stack = []
        for c in s: 
            if c in pdict:
                if stack and stack[-1] == pdict[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False
