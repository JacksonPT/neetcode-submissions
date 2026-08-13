class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        R = len(numbers) - 1
        L = 0

        while L < R:
            cur = numbers[L] + numbers[R]
            
            if cur == target:
                return [L+1, R+1]
            
            elif cur > target:
                R -= 1 
            else:
                L += 1
        
        return []