class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        oddfw, oddbw = [0] * n, [0] * n
        evenfw, evenbw = [0] * n, [0] * n
        for i in range(1, n):
            if (i-1) % 2 == 1:
                oddfw[i] = oddfw[i-1] + nums[i-1]
                evenfw[i] = evenfw[i-1]
            else:
                oddfw[i] = oddfw[i-1]
                evenfw[i] = evenfw[i-1] + nums[i-1]
        # print(oddfw, evenfw)
        for i in range(n-2, -1, -1):
            if (i+1) % 2 == 1:
                oddbw[i] = oddbw[i+1] + nums[i+1]
                evenbw[i] = evenbw[i+1]
            else:
                oddbw[i] = oddbw[i+1]
                evenbw[i] = evenbw[i+1] + nums[i+1]
        # print(oddbw, evenbw)
        cnt = 0
        for i in range(n):
            if oddfw[i] + evenbw[i] == evenfw[i] + oddbw[i]:
                # print(i)
                cnt += 1
        return cnt