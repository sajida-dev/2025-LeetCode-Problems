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
                per.append('0')
                rec(per)
                per.pop()
                per.append('1')
                rec(per)
                per.pop()
        rec([])
        return self.ans
