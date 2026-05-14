class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict = {}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in hashDict:
                return [hashDict[diff],i]
            hashDict[n] = i
        return []