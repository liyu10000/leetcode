# first try: almost brute force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            target = - nums[i]
            d = {}
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in d:
                    res.add((nums[i], diff, nums[j]))
                else:
                    d[nums[j]] = j
        return list(res)


# second try: use a dict to make judgement (runs fast, takes memory)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
                
        keys = list(d.keys())
        lk = len(keys)
        res = set()
        
        if 0 in d and d[0] > 2:
            res.add((0, 0, 0))
        
        for i in range(lk):
            x = keys[i]
            if x != 0 and d[x] > 1 and -2*x in d:
                r = [x, x, -2*x]
                r.sort()
                res.add(tuple(r))
            for j in range(i+1, lk):
                y = keys[j]
                if -(x+y) in d and -(x+y) not in [x, y]:
                    r = [x, y, -(x+y)]
                    r.sort()
                    res.add(tuple(r))
        return res
                

# third try: use two pointers, slower than the second try
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

# brute force with twoSum, TLE
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = set()
        for i in range(len(nums)):
            twoIdxx = self.twoSum(nums, i, -nums[i])
            for twoIdx in twoIdxx:
                if twoIdx[0] > i and twoIdx[1] > i:
                    triplet = [nums[i], nums[twoIdx[0]], nums[twoIdx[1]]]
                    triplet.sort()
                    res.add(tuple(triplet))
        return res
        
    def twoSum(self, nums: List[int], skip: int, target: int) -> List[int]:
        twoIdxx = []
        diffmap = {}
        for i,n in enumerate(nums):
            if i == skip:
                continue
            if n in diffmap:
                twoIdxx.append([diffmap[n], i])
                del diffmap[n]
            else:
                diffmap[target - n] = i
        return twoIdxx