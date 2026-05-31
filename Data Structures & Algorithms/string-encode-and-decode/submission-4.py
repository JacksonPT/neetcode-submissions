class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += str(len(s)) + "#" + s
        return output
    def decode(self, s: str) -> List[str]:
        # 4#neet5#code 
        i = 0
        ret = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ret.append(s[i:j])
            i = j
        return ret 
            
                