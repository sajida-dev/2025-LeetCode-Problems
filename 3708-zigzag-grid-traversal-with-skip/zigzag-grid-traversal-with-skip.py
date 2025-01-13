class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid)):
            if(i%2!=0):
                j = len(grid[i])-1 if(len(grid[i])%2==0) else len(grid[i])-2
                
                while(j>=0):
                    ans.append(grid[i][j])
                    j -= 2

            else:
                j = 0
                while(j<len(grid[i])):
                    ans.append(grid[i][j])
                    j += 2
            #print(ans)
                    
        return ans