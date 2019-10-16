# first try
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for n in d:
            if d[n] == 1:
                return n
        return None

# second try
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for n in nums:
            one = ~two & (one ^ n)
            two = ~one & (two ^ n)
        return one