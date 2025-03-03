class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i,j=0,0
        gre = []
        equ = 0
        while(j<len(nums)):
            if(nums[j] > pivot):
                gre.append(nums[j])
            elif(nums[j] == pivot):
                equ += 1
            if(nums[j]<pivot):
                if(i!=j):
                    nums[i] = nums[j]
                    
                i += 1
            j += 1
        j = 0
        while(j<equ):
            nums[i] = pivot
            i,j = i+1,j+1
        j = 0
        while(j<len(gre)):
            nums[i] = gre[j]
            i,j=i+1,j+1
        return nums