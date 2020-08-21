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