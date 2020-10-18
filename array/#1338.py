class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = defaultdict(int)
        for n in arr:
            count[n] += 1
        sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        currn = len(arr)
        res = 0
        for n,c in sort_count:
            if currn > len(arr) / 2:
                res += 1
                currn -= c
            else:
                break
        return res