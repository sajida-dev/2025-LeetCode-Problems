class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOperation =0
        n=len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = nums[i+1] ^ 1
                nums[i+2] = nums[i+2] ^ 1
                minOperation +=1
        if nums.count(0) > 0:
            minOperation = -1
        return minOperation
        