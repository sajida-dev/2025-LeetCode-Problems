class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        colors = {}
        balls = {}        
        for i, query in enumerate(queries):
            ball,color = query
            if(ball in balls):
                col = balls[ball]
                colors[col] -=1
                if(colors[col] == 0):
                    colors.pop(col)

            balls[ball] = color
            colors[color] = 1 if(color not in colors) else colors[color]+1
            #print(colors,balls)
            ans[i] = len(colors)
        return ans