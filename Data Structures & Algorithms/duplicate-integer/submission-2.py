class Solution:
    def hasDuplicate(self, nums):
        hashSet = set()
        for x in nums:
            if x in hashSet:
                return True
            else:
                hashSet.add(x)
        return False