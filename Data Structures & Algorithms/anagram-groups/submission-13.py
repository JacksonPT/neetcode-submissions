class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTab = defaultdict(list)
    
        ret = []

        for word in strs:
            sort = ''.join(sorted(word))
            hashTab[sort].append(word)
        
        if hashTab:
            for v in hashTab.values():
                ret.append(v)

        
        return ret


