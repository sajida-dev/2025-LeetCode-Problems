from sortedcontainers import SortedList
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
                dic[sumVal][1].add(x)
            else:
                dic[sumVal] = [1,SortedList([x])]
        ans = -1
        for val in dic.values():
            if(val[0]>=2):
                sumVal = val[1][-1]+val[1][-2]
                if(sumVal > ans):
                    ans = sumVal
        return ans