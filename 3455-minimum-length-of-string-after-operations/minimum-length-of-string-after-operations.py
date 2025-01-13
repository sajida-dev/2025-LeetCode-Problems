class Solution:
    def minimumLength(self, s: str) -> int:
        dic = {}
        for a in s:
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
        #print(dic)
        ans = 0
        for key in dic.keys():
            if(dic[key]>3):
                if(dic[key]%2==0):
                    ans += 2
                else:
                    ans += 1
            elif(dic[key] == 3):
                ans+=1
            else:
                ans += dic[key]
            
        return ans
        aaaaaaa