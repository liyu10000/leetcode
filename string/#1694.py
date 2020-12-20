class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        n = len(number)
        s = ''
        i = 0
        while n-i > 4:
            s += number[i:i+3] + '-'
            i += 3
        if n-i == 4:
            s += number[i:i+2] + '-'
            i += 2
        s += number[i:]
        return s