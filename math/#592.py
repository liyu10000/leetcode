class Solution:
    def fractionAddition(self, expression: str) -> str:
        # retrieve numerators and denominators
        nums, denoms, signs = [], [], []
        n = len(expression)
        i = 0
        if expression[i] != '-':
            signs.append('+')
        while i < n:
            if expression[i] in '+-':
                signs.append(expression[i])
                i += 1
            else:
                j = i
                while expression[j] != '/':
                    j += 1
                nums.append(int(expression[i:j]))
                j += 1
                i = j
                while j < n and expression[j] not in '+-':
                    j += 1
                denoms.append(int(expression[i:j]))
                i = j
        print(nums, denoms, signs)
        # calculate self-out-others products
        n = len(signs)
        products = []
        denom = 1
        for i in range(n):
            denom *= denoms[i]
        for i in range(n):
            products.append(denom // denoms[i])
        # merge fractions
        num = 0
        for i in range(n):
            if signs[i] == '+':
                num += nums[i] * products[i]
            else:
                num -= nums[i] * products[i]
        print(num, denom)
        # reduction
        for p in [2, 3, 5, 7, 11]:
            while num % p == 0 and denom % p == 0:
                num = num // p
                denom = denom // p
        return str(num) + '/' + str(denom)