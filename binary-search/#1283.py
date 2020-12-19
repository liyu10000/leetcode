class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        i, j = 1, max(nums)
        while i < j:
            m = (i + j) // 2
            c = 0
            for n in nums:
                c += n // m + (1 if n % m != 0 else 0)
            # print(m, c)
            if c > threshold:
                i = m + 1
            else:
                j = m
        return j