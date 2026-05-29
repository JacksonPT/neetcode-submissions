class Solution:

    def encode(self, strs: List[str]) -> str:
        retS = ""
        for x in strs:
            retS = retS + "`" + x
        return retS
    def decode(self, s: str) -> List[str]:
        retL = s.split("`")
        retL.pop(0)
        return retL
