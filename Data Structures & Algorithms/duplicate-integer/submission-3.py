class Solution:
    def hasDuplicate(self, nums):
        hashSet = set()
        for x in nums:
            if x not in hashSet:
                hashSet.add(x)
            else:
                return True
        return False