class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        # create two arrays to store:
        arr1 = [0] * n  # num of b before the index
        arr2 = [0] * n  # num of a after the index
        # loop forward to get arr1
        for i in range(1, n):
            arr1[i] = arr1[i-1] + (1 if s[i-1] == 'b' else 0)
        # loop backward to get arr2
        for i in range(n-2, -1, -1):
            arr2[i] = arr2[i+1] + (1 if s[i+1] == 'a' else 0)
        # take minimum sum
        dels = n
        for i in range(n):
            dels = min(dels, arr1[i]+arr2[i])
        return dels