class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for i, n in count.items():
            freq[n].append(i)
        
        res = []
        for x in range(len(freq)-1, 0, -1):
            for y in freq[x]:
                res.append(y)
                if len(res) == k:
                    return res
        