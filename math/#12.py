class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        
        res += 'M' * (num//1000)
        num = num % 1000

        if num >= 900:
            res += 'CM'
        elif num >= 500:
            res += 'D' + 'C' * ((num - 500) // 100)
        elif num >= 400:
            res += 'CD'
        else:
            res += 'C' * (num // 100)
        num = num % 100
        
        if num >= 90:
            res += 'XC'
        elif num >= 50:
            res += 'L' + 'X' * ((num - 50) // 10)
        elif num >= 40:
            res += 'XL'
        else:
            res += 'X' * (num // 10)
        num = num % 10
        
        if num == 9:
            res += 'IX'
        elif num >= 5:
            res += 'V' + 'I' * (num - 5)
        elif num == 4:
            res += 'IV'
        else:
            res += 'I' * num
            
        return res
        