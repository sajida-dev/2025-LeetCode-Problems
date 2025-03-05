class Solution:
    def coloredCells(self, n: int) -> int:
        totalColored = 1
        for i in range(2, n+1):
            if(i-2 > 0):
                totalColored += ((i-2)*4)
            totalColored += 4
        return totalColored