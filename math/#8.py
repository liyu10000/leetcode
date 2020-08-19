class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN, INT_MAX = - 2 ** 31, 2 ** 31 - 1
        len_ = len(str)
        i = 0
        while i < len_ and str[i] == ' ':
            i += 1
        # empty or all whitespace characters
        if i == len_:
            return 0
        # not a valid integral number
        if str[i] not in "+-0123456789":
            return 0
        # process potential integer
        flag = 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            flag = -1
            i += 1
        num = 0
        while i < len_ and str[i].isdigit():
            num = num * 10 + int(str[i])
            if flag == 1 and num >= INT_MAX:
                return INT_MAX
            if flag == -1 and num >= INT_MAX+1:
                return INT_MIN
            i += 1
        return flag * num