class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        rsum = 0 # running sum of to-be-kept letters
        n = len(s)
        i, j = 0, 0
        while j < n:
            cmax = cost[i] # current max of repeated letters
            while j + 1 < n and s[j] == s[j+1]:
                j += 1
                cmax = max(cmax, cost[j])
            rsum += cmax
            i, j = j + 1, j + 1
        return sum(cost) - rsum