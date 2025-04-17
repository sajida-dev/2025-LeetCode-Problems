from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        ans = 0
        for i in range(len(nums)):
            dic[nums[i]].append(i) 
        for key,val in dic.items():
            n = len(val)
            if(n > 2):
                for i in range(n):
                    for j in range(i+1, n):
                        if((val[i] * val[j]) % k == 0):
                            ans += 1
            elif(n == 2):
                if((val[0]*val[1]) % k == 0):
                    ans += 1
        return ans

