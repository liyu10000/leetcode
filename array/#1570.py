class SparseVector:
    def __init__(self, nums: List[int]):
        # self.n = len(nums)
        self.idx = []
        self.num = []
        for i,n in enumerate(nums):
            if n:
                self.idx.append(i)
                self.num.append(n)        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p = 0
        i, j = 0, 0
        n1, n2 = len(self.idx), len(vec.idx)
        while i < n1 or j < n2:
            if i == n1 or j == n2:
                break
            if self.idx[i] == vec.idx[j]:
                p += self.num[i] * vec.num[j]
                i += 1
                j += 1
            elif self.idx[i] < vec.idx[j]:
                i += 1
            else:
                j += 1
            # print(i, j)
        return p