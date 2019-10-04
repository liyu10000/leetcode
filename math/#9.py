class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x)
        return x[::-1] == x # reverse string and compare