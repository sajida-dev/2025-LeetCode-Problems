class Solution:
    def minimumLength(self, s: str) -> int:
        dic = [0]*26
        for a in s:
            dic[ord(a)-ord('a')] += 1
        
        ans = 0
        for val in dic:
            if(val>3):
                ans += 2 if(val%2==0) else 1
            elif(val == 3):
                ans+=1
            else:
                ans += val
        return ans