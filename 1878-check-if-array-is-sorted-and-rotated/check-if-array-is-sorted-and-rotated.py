class Solution:
    def check(self, nums: List[int]) -> bool:
        ind, minInd = 0,0
        for i in range(len(nums)):
            if nums[i] > nums[ind]:
                ind = i
            if(nums[i] < nums[minInd]):
                minInd = i
            #elif(nums[i] == nums[ind] and )

        act = nums[ind+1:] + nums[:ind+1]
        minAct = nums[minInd:] + nums[:minInd]
        sortVal = sorted(nums)
        #print(act,minAct,sortVal)
        if(act == sortVal or minAct ==sortVal):
            return True
        return False
        
            