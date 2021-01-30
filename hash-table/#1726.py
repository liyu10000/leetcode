class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prods = defaultdict(int)
        for i in range(n-1):
            for j in range(i+1, n):
                prods[nums[i]*nums[j]] += 1
        res = 0
        for p, c in prods.items():
            if c > 1:
                res += c * (c - 1) // 2
        return res * 8