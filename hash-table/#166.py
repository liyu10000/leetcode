class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        integer, mod = divmod(numerator, denominator)
        integer = str(integer)
        
        fracdict = {}
        fraction = ''
        i = 0
        while mod > 0:
            if mod in fracdict:
                fraction = fraction[:fracdict[mod]] + '(' + fraction[fracdict[mod]:] + ')'
                break
            else:
                fracdict[mod] = i
                div, mod = divmod(mod*10, denominator)           
                fraction += str(div)
                i += 1
        
        return sign + integer + ('.' if fraction else '') + fraction