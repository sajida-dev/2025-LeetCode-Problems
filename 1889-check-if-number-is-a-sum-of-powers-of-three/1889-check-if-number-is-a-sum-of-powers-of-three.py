class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        self.ans = False
        squ = [1]
        totalSum = 1
        while(totalSum < n):
            squ.append(squ[-1]*3)
            totalSum += squ[-1]
        def rec(squ , sumVal):
            if(not squ or sumVal > n):
                if(sumVal == n):
                    self.ans = True
                return
            if(not self.ans):
                rec(squ[1:], sumVal + squ[0])
            if(not self.ans):
                rec(squ[1:], sumVal)
        rec(squ,0)
        return self.ans