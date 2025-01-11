class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if(len(s) == k):
            return True
        elif(len(s) < k):
            return False
        dic = {}
        for a in s:
            if(a not in dic): 
                dic[a] = 1 
            else:
                dic[a]+=1
        print(dic)
        singleElement = 0
        words = 0
        for key in dic.keys():
            if dic[key]%2!=0: # odd
                singleElement += 1
                if(dic[key] > 1):
                    words += dic[key]-1
            else: #even
                words += dic[key]
            if(singleElement > k):
                return False

        if((words + singleElement)  < k):
            return False
        return True
        