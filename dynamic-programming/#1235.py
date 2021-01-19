# dp, with O(n) = n^2, get TLE
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[s,e,p] for s,e,p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda job:job[1])
        n = len(jobs)
        dp = [0] * (n+1) # dp[i] means profit gained at end of ith job
        for i in range(n):
            dp[i+1] = max(dp[i], jobs[i][2])
            for j in range(i):
                if jobs[j][1] <= jobs[i][0]:
                    dp[i+1] = max(dp[i+1], dp[j+1]+jobs[i][2])
        # print(dp)
        return dp[n]

# use binary search to find the point j
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[s,e,p] for s,e,p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda job:job[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]