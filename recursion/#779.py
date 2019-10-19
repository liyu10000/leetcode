import math

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        memo = {(1, 1): 0}
        
        def find(n, k):
            if (n, k) in memo:
                return memo[(n, k)]
            if k == 1:
                return 0
            
            t = find(n-1, math.ceil(k/2))
            if t == 0:
                if k % 2 == 0:
                    return 1
                else:
                    return 0
            else:
                if k % 2 == 0:
                    return 0
                else:
                    return 1
        
        return find(N, K)