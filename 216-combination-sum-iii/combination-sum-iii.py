class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        visit = [False]*9
        def backtrack(sumVal,visit,res):
            if(len(res)+1 == k):
                val = n-sumVal
                if((0 < val<= 9) and (not visit[val-1])):
                    res = res+[val]
                    res.sort()
                    if(not res in self.ans):
                        self.ans.append(res)
                return
            for i in range(1,10):
                if(not visit[i-1]):
                    visit[i-1] = True
                    backtrack(sumVal+i,visit,res+[i])
                    visit[i-1] = False
        for i in range(1,10):
            visit[i-1]=True
            backtrack(i,visit,[i])
            visit[i-1] = False
        return self.ans