class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n,m,k = len(nums2),len(nums1),0
        num1,num2=0,0
        ans = 0
        for val in nums1:
            num1 ^= val
        print(num1)
        for val in nums2:
            num2 ^= val
        print(num2)
        if(n%2==0):
            num1 = 0
        if(m%2==0):
            num2 = 0

        return num1^num2
        