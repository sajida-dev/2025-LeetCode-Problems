class Solution:
    def coloredCells(self, n: int) -> int:
        return ((n-1)*4)+1+((((n-1)*(n-2))//2)*4)
