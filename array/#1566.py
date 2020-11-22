class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n-m*k+1):
            flag = True
            for j in range(m):
                iflag = True
                for t in range(1, k):
                    # print(i, j, t)
                    if arr[i+j] != arr[i+j+t*m]:
                        iflag = False
                        flag = False
                        break
                if not iflag:
                    break
            if flag:
                return True
        return False

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        cnt = 0
        for i in range(n-m):
            if arr[i] != arr[i+m]:
                cnt = 0
            cnt += (arr[i] == arr[i+m])
            if cnt == m * (k-1):
                return True
        return False