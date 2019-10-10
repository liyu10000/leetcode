# first try: brute force, time limit exceeded
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i, (g, c) in enumerate(zip(gas, cost)):
            if g < c:
                continue
            else:
                carry = gas[i] - cost[i]
                for j in list(range(i+1, len(gas))) + list(range(0, i)):
                    carry += gas[j] - cost[j]
                    if carry < 0:
                        break
                if carry >= 0:
                    return i
        return -1

# second try: 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        index = -1
        tank = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            if tank + g >= c:
                if tank == 0:
                    index = i
                tank += g - c
            else:
                tank = 0
                index = -1
        return index