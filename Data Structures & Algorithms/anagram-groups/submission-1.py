class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anCheck = defaultdict(list)

        for x in strs:
            checkLet = [0] * 26

            for c in x:
                checkLet[ord(c) - ord("a")] += 1

            anCheck[tuple(checkLet)].append(x)
        return list(anCheck.values())


