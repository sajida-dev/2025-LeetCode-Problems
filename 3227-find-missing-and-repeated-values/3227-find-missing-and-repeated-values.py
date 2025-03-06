class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ar = [0]*(n*n)
        repeating = 0
        for row in grid:
            for val in row:
                ar[val-1] += 1
                if(ar[val-1]==2):
                    repeating = val
        miss = ar.index(0)+1
        return [repeating,miss]
