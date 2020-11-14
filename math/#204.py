# brute force, TLE
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = set()
        for i in range(2, n):
            if i == 2 or i == 3:
                primes.add(i)
            else:
                flag = True
                for p in primes:
                    if i % p == 0:
                        flag = False
                        break
                if flag:
                    primes.add(i)
        # print(primes)
        return len(primes)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if not isPrime[i]:
                continue
            for j in range(i*i, n, i):
                isPrime[j] = False
            i += 1
        cnt = 0
        for i in range(2, n):
            if isPrime[i]:
                cnt += 1
        return cnt