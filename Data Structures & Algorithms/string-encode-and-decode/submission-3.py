class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for x in strs:
            length = len(x)
            output = output + str(length) + "#" + x
        return output

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1:j + 1 + length]
            final.append(word)

            i = j + 1 + length

        return final