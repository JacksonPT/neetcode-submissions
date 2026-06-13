class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapX = defaultdict(int)
        hashMapY = defaultdict(int)
        for x in s:
            hashMapX[x] += 1
        for x in t:
            hashMapY[x] += 1
        
        for key in hashMapX.keys():
            if hashMapX[key] != hashMapY[key]:
                return False
        for key in hashMapY.keys():
            if hashMapX[key] != hashMapY[key]:
                return False
        return True

            