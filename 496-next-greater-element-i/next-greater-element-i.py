class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = [nums2[-1]]
        dic = {}
        n = len(nums2)
        ans = [-1]*len(nums1)
        for i in range(n-2, -1, -1):
            while(st and st[-1] <= nums2[i]):
                st.pop()
            if st:
                dic[nums2[i]] = st[-1]
            st.append(nums2[i])
        for i in range(len(nums1)):
            if(nums1[i] in dic):
                ans[i] = dic[nums1[i]]

        return ans
                