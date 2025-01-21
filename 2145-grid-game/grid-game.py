import copy
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pre = copy.deepcopy(grid)
        n=len(grid[0])
        if(n==1):
            return 0
        for i in range(2,n):
            pre[0][i] += pre[0][i-1]
            pre[1][n-1-i] += pre[1][n-i]
        collection = min(pre[0][-1],pre[1][0])
        for i in range(1,n-1):
            collection = min(collection,max(pre[0][-1]-pre[0][i],pre[1][0]-pre[1][i]))
        return collection
        