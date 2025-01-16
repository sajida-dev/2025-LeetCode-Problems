class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n,m,k = len(nums2),len(nums1),0
        ans = 0
        for i in range(m):
            for j in range(n):
                ans ^= nums1[i]^nums2[j]
                k+=1
        
        return ans