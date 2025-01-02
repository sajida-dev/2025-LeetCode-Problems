class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        test = ""
        check = ""
        n,x,m=len(s),0,0
        if n == 1:
            return s
        elif n == 2:
            if s[0] == s[1]:
                return s
            else:
                check = s[0]
                return check
        for j in range(n):
            test = ""
            if (n - j <= m):
                break
            for i in range(j,n):
                test += s[i]
                
                if test[::-1] == test:
                    x,m = len(test),len(max_pal)
                    if x > m:
                        max_pal = test
        return max_pal