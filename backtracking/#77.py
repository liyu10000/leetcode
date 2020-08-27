class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(s, curr):
            if len(curr) == k:
                output.append(curr[:])
            else:
                for i in range(s, n):
                    curr.append(i+1)
                    backtrack(i+1, curr)
                    curr.pop()
        output = []
        backtrack(0, [])
        return output


class Solution:
    res = []
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, 1, k, [])
        return self.res
    
    def backtrack(self, n, i, k, cur):
        if k == 0:
            self.res.append(cur)
        for j in range(i, n+1):
            self.backtrack(n, j+1, k-1, cur+[j])

