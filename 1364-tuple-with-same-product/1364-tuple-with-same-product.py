class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = {}       
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                val = nums[i]*nums[j]
                if(val in dic):
                    dic[val] += 1
                else:
                    dic[val] = 1
        res = 0
        for key in dic:
            if(dic[key] == 2):
                res += 1
            elif(dic[key] > 2):
                n=dic[key]
                res += ((n*(n-1))//2)
        return res*8