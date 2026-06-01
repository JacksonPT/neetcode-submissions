class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def productList(L: List[int]):
            prod = 1
            for x in L:
                prod = prod * x
            return prod

        ret = []
        for n in nums:
            newList = nums.copy()
            newList.remove(n)
            ret.append(productList(newList))

        return ret
