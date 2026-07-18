class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        theSet = set(nums)
        longest = 0

        #loop through numbers
        for x in theSet:
            #if a number is the start of a sequence and has not been added , add
            if x-1 not in theSet:
                length = 1
                while x + length in theSet:
                    length += 1
                longest = max(length,longest)

        
        
        
        return longest
