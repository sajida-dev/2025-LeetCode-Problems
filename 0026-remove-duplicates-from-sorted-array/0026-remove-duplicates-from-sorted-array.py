class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while(j < len(nums)):
            if(nums[i] != nums[j]):
                nums[i+1] = nums[j]
                i+=1
            j+=1
        return i+1

       # i       j
# [0,2,3,4,3,3,4]
# [0,1,2,3,4,2,2,3,3,4]
# 5

