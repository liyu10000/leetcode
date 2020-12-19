# use two hashsets
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        d = set()
        for n in nums:
            if n-k in d:
                pairs.add((n-k, n))
            if n+k in d:
                pairs.add((n, n+k))
            d.add(n)
        return len(pairs)

# use a hash map to record count
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        ns = list(d.keys())
        ns.sort()
        cnt = 0
        for n in ns:
            if k > 0 and n+k in d:
                cnt += 1
            if k == 0 and d[n] > 1:
                cnt += 1
        return cnt