class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [0 for _ in range(26)]
        for task in tasks:
            arr[ord(task) - ord('A')] += 1
        arr.sort(reverse=True)
        maxlen = arr[0]
        gap = (maxlen - 1) * n
        length = gap + maxlen
        for i in range(1, 26):
            if gap >= arr[i]:
                if arr[i] == maxlen:
                    gap -= (maxlen - 1)
                    length += 1
                else:
                    gap -= arr[i]
            else:
                return len(tasks)
        return length