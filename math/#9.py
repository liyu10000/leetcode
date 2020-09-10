# convert to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x)
        return x[::-1] == x # reverse string and compare


# reverse integer to the half point to check if two numbers equal
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10==0 and x != 0):
            return False
        y = 0
        while x >= 0:
            tmpy = y * 10 + x % 10
            x //= 10
            if x == y or x == tmpy:
                return True
            y = tmpy
            if x < y:
                return False
        return False