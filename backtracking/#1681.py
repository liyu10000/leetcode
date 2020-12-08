class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        if any(f[num] > k for num in f):
            return -1
        bags = [[] for i in range(k)]
        res = float("inf")
        n = len(nums)
        M = n // k
        nums.sort()
        
        ### DFS put #i number in #j bag
        def DFS(i,cur_res):
            nonlocal res
            if i == n:
                res = min(res,cur_res)
                return
            if cur_res + (n+1-i) >= res  : ### (n+1-i) numbers left and each number would make cur_res increase at least one =>  final_res(i reaches n) in this branch >= cur_res + (n+1-i)*1
                return 
            
            for j in range(k):
                ### skip when 1. encounter same combination 2. avoid duplicate number in some bags 3. bag is full
                if (j > 0 and bags[j] == bags[j-1]) or (bags[j] and bags[j][-1] == nums[i]) or (len(bags[j]) == M):
                    continue
                else:
                    bags[j].append(nums[i])
                    if len(bags[j]) == 1:
                        DFS(i+1,cur_res)
                    else:
                        DFS(i+1,cur_res+bags[j][-1]-bags[j][-2])
                    bags[j].pop()                
        DFS(0,0)
        return res