# O(n^2), get TLE
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counts = defaultdict(int)
        for d in deliciousness:
            counts[d] += 1
        keys = list(counts.keys())
        n = len(keys)
        res = 0
        # check distinct
        for i in range(n-1):
            for j in range(i+1, n):
                if self.isPowerOfTwo(keys[i] + keys[j]):
                    res += counts[keys[i]] * counts[keys[j]]
        # check same value
        for d in keys:
            if counts[d] > 1 and self.isPowerOfTwo(d + d):
                res += counts[d] * (counts[d] - 1) // 2
        return res % (10 ** 9 + 7)
                
    # Function to check if x is power of 2
    def isPowerOfTwo(self, x):

        # First x in the below expression 
        # is for the case when x is 0 
        return x and (not(x & (x - 1)))

# check diff
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powerTwo = [2 ** i for i in range(22)]
        counts = defaultdict(int)
        for d in deliciousness:
            counts[d] += 1
        res = 0
        for d, c in counts.items():
            for p in powerTwo:
                if 2*d <= p and p - d in counts:
                    if d == p - d:
                        res += c * (c - 1) // 2
                    else:
                        res += c * counts[p - d]
        return res % (10 ** 9 + 7)