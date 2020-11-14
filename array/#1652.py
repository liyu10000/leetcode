class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        flag = False
        if k < 0:
            flag = True
            code.reverse()
            k = -k
        arr = []
        rsum = 0
        for i in range(n):
            if i == 0:
                rsum = sum(code[1:1+k])
            elif i + k < n:
                rsum = rsum - code[i] + code[i+k]
            else:
                rsum = rsum - code[i] + code[i+k-n]
            arr.append(rsum)
        if flag:
            arr.reverse()
        return arr