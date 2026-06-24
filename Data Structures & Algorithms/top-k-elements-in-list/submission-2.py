class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM = defaultdict(list)
        for x in list(set(nums)):
            hashM[nums.count(x)].append(x)
        #{2: [7] {count: num}}

        ret = []
        for count in range(len(nums), 0, -1):
                if len(ret) == k:
                    break 

                if count in hashM:
                    for x in hashM[count]:
                        if len(ret) == k:
                            break 
                        ret.append(x)
        
        return ret