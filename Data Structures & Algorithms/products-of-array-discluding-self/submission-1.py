import math
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 8 24
        new = []
        for x in nums:
            copy = nums.copy()
            copy.remove(x)
            new.append(math.prod(copy))
        
        return new
        
