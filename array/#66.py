class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for d in digits[::-1]:
            res.append((d + carry) % 10)
            carry = (d + carry) // 10
        if carry > 0:
            res.append(carry)
        return res[::-1]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = []
        d = 1
        for i in range(len(digits)-1, -1, -1):
            d += digits[i]
            out.append(d % 10)
            d //= 10
        if d > 0:
            out.append(d)
        out.reverse()
        return out

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + 1
            if tmp != 10:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits