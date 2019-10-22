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