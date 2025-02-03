class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc,dec,maxInc,maxDec = 1,1,1,1
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                inc += 1
                dec = 1
            elif(nums[i] > nums[i+1]):
                dec += 1
                inc = 1
            else:
                inc,dec = 1,1
            if(inc > maxInc):
                maxInc = inc
            if dec > maxDec:
                maxDec = dec
            #print("inc : ",inc,"\ndec : ",dec,"\nmaxDec : ",maxDec, "\nmaxInc : ", maxInc)
        return maxInc if(maxInc > maxDec) else maxDec