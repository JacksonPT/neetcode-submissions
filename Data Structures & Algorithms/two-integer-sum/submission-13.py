class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     has = {}
     for i, v in enumerate(nums):
        diff = target - v
        if v in has:
            return [has[v], i]
        has[diff] = i
     return []

     #hashmap = {diff : index }
     #{4:0, }
     #