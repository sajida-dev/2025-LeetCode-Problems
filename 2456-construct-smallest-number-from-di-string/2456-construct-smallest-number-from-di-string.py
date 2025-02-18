class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = [0]*(n+1)
        i, ind, pre = 0, 1, -1
        while(i < n):
            if(pattern[i] == 'I'):
                ans[i] = str(ind)
                ind += 1
            else:
                if(i+1 < n and pattern[i+1] == 'I'):
                    pre = i+1
                    ans[i+1] = str(ind)
                    ans[i] = str(ind+1)
                    ind += 2
                    i-=1
                    while(i>=0 and pattern[i] != 'I'):
                        ans[i] = str(ind)
                        ind += 1
                        i-=1
                    i = pre
            i += 1
        i = n-1
        if(ans[-1] == 0):
            ans[-1] = str(ind)
            ind += 1
            while(i>=0 and pattern[i]!= 'I' and ans[i]==0):
                ans[i] = str(ind)
                ind += 1
                i-=1                
        return "".join(ans)
