class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        while i < len(str):
            if str[i] == ' ':
                i += 1
            else:
                break
        if i == len(str):
            return 0
        
        if str[i] not in '+-0123456789':
            return 0
        
        sign = 1
        if str[i] == '+':
            sign = 1
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1
        
        res = 0
        while i < len(str):
            if str[i] not in '0123456789':
                break
            d = int(str[i])
            res = res * 10 + d
            i += 1
        res = res * sign
        
        INT_MAX = 2 ** 31 -1
        INT_MIN = - 2 ** 31
        if res > INT_MAX:
            res = INT_MAX
        if res < INT_MIN:
            res = INT_MIN
        
        return res