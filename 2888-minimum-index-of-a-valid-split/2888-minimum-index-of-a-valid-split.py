class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        splitFreq = 0
        for i in range(n):
            if(nums[i] in dic):
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        dominent = nums[0]
        for key in dic:
            if(dic[key] > dic[dominent]):
                dominent = key
        freq = dic[dominent]
        # print(dominent,freq)
        # print(dic)
        for i in range(n):
            if(nums[i] == dominent):
                splitFreq += 1
            if(splitFreq*2 > i+1 and (freq-splitFreq)*2>n-(i+1)):
                return i
            # print(splitFreq,splitFreq*2,i+1,i,freq-splitFreq,(freq-splitFreq)*2,n-(i+1))
        return -1
        