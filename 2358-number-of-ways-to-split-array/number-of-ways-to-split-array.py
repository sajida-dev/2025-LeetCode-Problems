class Solution:
    def waysToSplitArray(self, preSum: List[int]) -> int:
        n = len(preSum)
        preSum[0] = preSum[0]
        for i in range(1,n):
            preSum[i] = preSum[i-1] + preSum[i]
        print(preSum)
        ans = 0
        for i in range(n-1):
            if(preSum[i] >= (preSum[n-1]-preSum[i])):
                ans += 1
        return ans