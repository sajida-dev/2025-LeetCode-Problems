from sortedcontainers import SortedList
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if(s[i] not in dic):
                dic[s[i]] = []
            dic[s[i]].append(i)
        print(dic)
        ans = 0
        for key, val in dic.items():
            l , r = val[0], val[-1]
            ans += len(set(s[l+1:r]))
        return ans