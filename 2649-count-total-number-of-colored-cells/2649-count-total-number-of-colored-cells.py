class Solution:
    def coloredCells(self, n: int) -> int:
        totalColored, diagonalCells = 1,0
        for i in range(2, n+1):
            if(i >= 3):
                diagonalCells += 4
            totalColored += (4 + diagonalCells)
        return totalColored