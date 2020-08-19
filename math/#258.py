class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        new_num = 0
        while num > 0:
            new_num += num % 10
            num //= 10
        return self.addDigits(new_num)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num-1) % 9