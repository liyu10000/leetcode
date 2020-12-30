# use hash map, loop through all keys each time, get TLE
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sumMap = defaultdict(int)
        preSum = 0
        cnt = 0
        for a in A:
            preSum += a
            if preSum % K == 0:
                cnt += 1
            for s,c in sumMap.items():
                if (preSum - s) % K == 0:
                    cnt += c
            sumMap[preSum] += 1
        return cnt

# use hash map, constrain keys in range [0, K)
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sumMap = defaultdict(int)
        preSum = 0
        cnt = 0
        for a in A:
            preSum += a
            preSum -= (preSum // K) * K
            if preSum == 0:
                cnt += 1
            if preSum in sumMap:
                cnt += sumMap[preSum]
            sumMap[preSum] += 1
            # print(preSum, cnt, sumMap)
        return cnt

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sumMap = defaultdict(int)
        preSum = 0
        cnt = 0
        for a in A:
            preSum = (preSum + a) % K
            if preSum == 0:
                cnt += 1
            if preSum in sumMap:
                cnt += sumMap[preSum]
            sumMap[preSum] += 1
            # print(preSum, cnt, sumMap)
        return cnt