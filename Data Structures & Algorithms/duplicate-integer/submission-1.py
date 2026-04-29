class Solution:
    def hasDuplicate(self, nums):
        setList = set()

        for x in nums:
            if x in setList:
                return True
            else:
                setList.add(x)
        return False