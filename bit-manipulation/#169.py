# first try
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        count, num = 0, 0
        for n in d:
            if d[n] > count:
                count = d[n]
                num = n
        return num

# second try
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return list(c.keys())[list(c.values()).index(max(c.values()))]