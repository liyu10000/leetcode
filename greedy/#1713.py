class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        return len(target) - self.commonSubsequence(target, arr)
    
    def commonSubsequence(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if arr1[i] == arr2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[n1][n2]