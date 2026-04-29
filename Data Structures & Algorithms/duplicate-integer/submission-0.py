class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            for i in range(len(nums)):
                if x == nums[i] and nums.index(x) != i:
                    return True
        return False
            