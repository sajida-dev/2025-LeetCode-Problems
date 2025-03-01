class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i,countZero = 0,0
        while(i<len(nums)-1):
            if(nums[i] == nums[i+1]):
                nums[i] *= 2
                nums[i+1] = 0
                countZero += 1
                i+=1
            i+=1
        i,j = 0,0
        while(i<len(nums)):
            if(nums[i]!=0):
                if(i!=j):
                    nums[j],nums[i] = nums[i],0  
                j+=1    
            i+=1
        return nums
                

            
        
