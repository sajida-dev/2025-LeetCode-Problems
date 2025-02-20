class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count, self.ans = 1,""
        alpha = ['a','b','c']
        def rec(s):
            if(len(s) == n):
                if(self.count == k):
                    self.ans = "".join(s)
                    return self.ans
                self.count += 1
                return ""
            if(s):
                for val in alpha:
                    if(s[-1] != val and self.ans==""):
                        s.append(val)
                        rec(s)
                        s.pop()
            else:
                for val in alpha:
                    if(self.ans == ""):
                        s.append(val)
                        rec(s)
                        s.pop()
        rec([])
        return self.ans