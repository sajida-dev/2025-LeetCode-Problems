class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while(part in s):
            ind = s.index(part)
            s = s[:ind] + s[ind+len(part):]
            #print(s)
        return s