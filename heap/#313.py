# first try
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        n_ps = len(primes)
        index = [0] * n_ps
        nums = [1]
        for _ in range(1, n):
            minn = min([nums[index[i]]*primes[i] for i in range(n_ps)])
            nums.append(minn)
            for i in range(n_ps):
                if minn == nums[index[i]]*primes[i]:
                    index[i] += 1
        return nums[-1]


# second try
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglyList = [1]
        
        def gen(prime):
            for u in uglyList:
                yield u * prime
                
        mergeList = heapq.merge(*map(gen, primes))
        
        while len(uglyList) < n:
            uglyNum = next(mergeList)
            if uglyNum != uglyList[-1]:
                uglyList.append(uglyNum)
                
        return uglyList[-1]