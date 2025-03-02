class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for key,val in nums1:
            dic[key] = val
        for key,val in nums2:
            if(key in dic):
                dic[key] += val
            else:
                dic[key] = val
        ans = []
        for row in sorted(dic.items()):
            ans.append([row[0],row[1]])
        return ans