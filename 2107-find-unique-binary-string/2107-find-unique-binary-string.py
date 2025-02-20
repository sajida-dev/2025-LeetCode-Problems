class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        dic = {}
        n = len(nums[0])   
        for val in nums:
            dic[val] = True
        self.ans = ""
        def rec(per):
            if(len(per) == n):
                s = "".join(per)
                if(s not in dic):
                    self.ans = s
                    return s
                return ''
            if(self.ans==''):
                rec(per+['0'])
                rec(per+['1'])
        rec([])
        return self.ans
