class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in dictionary:
                return [dictionary[diff], i]
            dictionary[x] = i
        return []