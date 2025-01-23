class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        col = [0]*len(grid[0])
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    col[j] += 1
        for i in range(len(grid)):
            count = grid[i].count(1)
            if(count>1):
                ans += count
            elif(count == 1):
                ind = grid[i].index(1)
                if(col[ind]>1):
                    ans += 1
        return ans