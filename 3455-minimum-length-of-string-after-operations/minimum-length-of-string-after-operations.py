class Solution:
    def minimumLength(self, s: str) -> int:
        dic = [0]*26
        for a in s:
            dic[ord(a)-ord('a')] += 1
        ans = 0
        for val in dic:
            if(val == 0):
                continue
            ans += (val-2) if(val%2==0) else (val-1)
        return len(s)-ans