# first try
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        f235 = [1, 1, 1]
        i235 = [0, 0, 0]
        count = 1
        nums = [1]
        while count < n:
            pool = [f235[0]*2, f235[1]*3, f235[2]*5]
            minn = min(pool)
            mini = pool.index(minn)
            if minn != nums[-1]:
                nums.append(minn)
                count += 1
            i235[mini] += 1
            f235[mini] = nums[i235[mini]]
        return nums[-1]

# second try
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        f = [2, 3, 5]
        i235 = [0, 0, 0]
        nums = [1]
        for _ in range(1, n):
            minn = min([nums[i235[i]]*f[i] for i in range(3)])
            nums.append(minn)
            for i in range(3):
                if minn == nums[i235[i]]*f[i]:
                    i235[i] += 1
        return nums[-1]
