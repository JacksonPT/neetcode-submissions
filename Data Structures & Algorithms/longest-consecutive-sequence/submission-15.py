class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        theSet = set(nums)
        longest = 0

        for x in theSet:
            if x-1 not in theSet:
                length = 1
                while x+1 in theSet:
                    length += 1
                    x += 1
                longest = max(length, longest)
        
        
        return longest
