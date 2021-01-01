# initial trial, passed 28 / 33.
import heapq

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num)
        if k == 0:
            return num
        if k == l:
            return '0'
        # count number of digits larger than right
        larger = [0] * l
        appeared = defaultdict(int)
        q = []
        for i in range(l-1, -1, -1):
            n = int(num[i])
            c = 0
            for j in range(n):
                c += appeared[j]
            larger[i] = c
            appeared[n] += 1
            heapq.heappush(q, [-c, i])
        # print(larger)
        # collect indices to remove
        remove = [0] * l
        while k > 0:
            c, i = heapq.heappop(q)
            # print(c, i)
            if c == 0:
                break
            remove[i] = 1
            k -= 1
        # when counts are all zeros, remove from right
        i = l - 1
        while k > 0:
            if remove[i] == 0:
                remove[i] = 1
                i -= 1
                k -= 1
        # build new str
        res = ''
        nonzero = False # mark if res has started
        for i in range(l):
            if remove[i] == 0:
                if num[i] != '0':
                    res += num[i]
                    nonzero = True
                elif nonzero:
                    res += num[i]
        return res if res else '0'


# Using stack and greedy
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        print(numStack, k)
        
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack
        
        # trim the leading zeros
        return "".join(finalStack).lstrip('0') or "0"