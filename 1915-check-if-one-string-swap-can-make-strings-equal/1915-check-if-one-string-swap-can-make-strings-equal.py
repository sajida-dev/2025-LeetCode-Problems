class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if(len(s1) == 1 and len(s2) == 1):
            if(s1 == s2):
                return True
        dic = [-1]*2
        ind = 0
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                if ind < 2:
                    dic[ind] = i
                    ind += 1
                else:
                    return False
        if ind == 2:
            if s1[dic[0]] == s2[dic[1]] and s2[dic[0]] ==s1[dic[1]]:
                return True
        return True if ind == 0 else False