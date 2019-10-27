class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x <= 3:
            return 1
        
        n = x // 2
        while n * n > x:
            n //= 2
        if n * n == x:
            return n
        else:
            l, r = n, n * 2
            while l <= r:
                mid = (l + r) // 2
                if mid * mid == x:
                    return mid
                elif mid * mid < x:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return mid if mid ** 2 < x else mid - 1