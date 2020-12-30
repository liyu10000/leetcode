class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # find a point that starts repeating
        statesMap = {}
        for i in range(N):
            key = ''.join([str(c) for c in cells])
            if key in statesMap:
                previ = statesMap[key]
                N = (N - previ) % (i - previ) + previ
                break
            statesMap[key] = i
            cells = self.oneStep(cells)
        # retrieve the cell
        for key,i in statesMap.items():
            if i == N:
                cells = [int(c) for c in key]
                break
        return cells
        
    def oneStep(self, cells):
        newcells = [0] * 8
        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                newcells[i] = 1
            else:
                newcells[i] = 0
        return newcells