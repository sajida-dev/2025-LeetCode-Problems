class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        for val in nums:
            sumVal = 0
            x = val
            while(val > 0):
                sumVal += val%10
                val = val//10
            if(sumVal in dic):
                dic[sumVal][0] += 1
                if(dic[sumVal][2] < dic[sumVal][1]):
                    if(dic[sumVal][2] < x):
                        dic[sumVal][2] = x
                else:
                    if(dic[sumVal][1] < x):
                        dic[sumVal][1] = x
            else:
                dic[sumVal] = [1,x,0]
        ans = -1
        for val in dic.values():
            if(val[0]>=2):
                sumVal = val[1]+val[2]
                if(sumVal > ans):
                    ans = sumVal
        return ans