# iterative search, get TLE
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = []
        for i in range(n):
            m = 1
            for j in range(i):
                if obstacles[j] <= obstacles[i]:
                    m = max(m, dp[j] + 1)
            dp.append(m)
        return dp

# binary search for `m = max(m, dp[j] + 1)`
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        for i, x in enumerate(obstacles):
            if len(lis) == 0 or lis[-1] <= x:  # Append to LIS if new element is >= last element in LIS
                lis.append(x)
                obstacles[i] = len(lis)
            else:
                idx = bisect_right(lis, x)  # Find the index of the smallest number > x
                lis[idx] = x  # Replace that number with x
                obstacles[i] = idx + 1
        return obstacles
