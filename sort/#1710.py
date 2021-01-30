class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda b:b[1], reverse=True)
        units = 0
        i = 0
        while truckSize and i < len(boxTypes):
            numberOfBoxesi, numberOfUnitsPerBoxi = boxTypes[i]
            u = min(truckSize, numberOfBoxesi)
            units += u * numberOfUnitsPerBoxi
            truckSize -= u
            i += 1
        return units