class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum, sumVal = 0,nums[0]
        for i in range(len(nums)-1):
            if(nums[i] < nums[i+1]):
                sumVal += nums[i+1]
            else:
                sumVal = nums[i+1]
            if(maxSum < sumVal):
                maxSum = sumVal
            #print(sumVal,maxSum)
            #print(nums[i],nums[i+1])
        
        return maxSum if maxSum > sumVal else sumVal