class Solution:
    def waysToSplitArray(self, preSum: List[int]) -> int:
        n = len(preSum)
        leftSum, rightSum = 0, sum(preSum)
        ans = 0
        for i in range(n-1):
            leftSum += preSum[i]
            if(leftSum >= (rightSum-leftSum)):
                ans += 1
        return ans