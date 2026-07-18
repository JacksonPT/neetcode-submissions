class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        theSet = defaultdict(List)
        countList = []
        if len(nums) == 0:
            return 0
        for x in nums:
            counter = 1
            while x+1 in nums:
                x += 1
                counter += 1
            countList.append(counter)
        
        return max(countList)
