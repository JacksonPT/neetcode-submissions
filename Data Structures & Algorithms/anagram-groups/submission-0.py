class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        identifyAn = defaultdict(list)
        for x in strs:
            count = [0] * 26

            for y in x:
                count[ord(y) - ord("a")] += 1

            identifyAn[tuple(count)].append(x)
        
        return list(identifyAn.values())

