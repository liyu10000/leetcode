class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0 for _ in range(len(nums)+1)]
        for i,n in enumerate(nums):
            self.dp[i+1] += self.dp[i] + n

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]

