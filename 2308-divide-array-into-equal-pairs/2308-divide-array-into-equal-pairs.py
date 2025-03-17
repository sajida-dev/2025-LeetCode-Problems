class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for num in nums:
            if(num in dic):
                dic[num] += 1
            else:
                dic[num] = 1
        for key in dic:
            if(dic[key] % 2 != 0):
                return False
        return True