class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = ((n*(n-1))//2)
        dic = {}
        for i in range(n):
            val = nums[i]-i
            if(val in dic):
                dic[val] += 1
            else:
                dic[val] = 1
        for key in dic:
            if(dic[key] > 1):
                m = dic[key]
                ans -= ((m*(m-1))//2)
        return ans