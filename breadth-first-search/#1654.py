class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        maxp = max(forbidden) + a + b + x  # set the limit the bug can jump to
        forbideen = set(forbidden)
        if x == 0:
            return 0
        if a in forbidden:
            return -1
        visited = set()
        queue = [(1,a)]  # direction (1 forward and 0 backward), position
        jumps = 0
        while queue:
            # print(jumps, queue)
            jumps += 1
            flag = 0 # flag to check if all existing positions are visited
            newqueue = []
            for d,y in queue:
                if y == x:
                    return jumps
                if (d,y) in visited:
                    flag += 1
                    continue
                visited.add((d,y))
                if y + a < maxp and not y + a in forbidden:
                    newqueue.append((1, y + a))
                if d and y - b > 0 and not y - b in forbidden:
                    newqueue.append((0, y - b))
            if flag == len(queue):
                return -1
            queue = newqueue
        return -1