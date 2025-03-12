class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        beg,end = 0, n-1
        mid = (beg+end)//2
        while(beg<=end and nums[mid] != -1):
            mid = (beg+end)//2
            if(nums[mid] > -1):
                end = mid - 1
            elif(nums[mid] < -1):
                beg = mid + 1
        beg = mid
        while(beg < n and nums[beg] <= 0):
            beg += 1
        while(mid >= 0 and nums[mid] >= 0):
            mid -= 1
        return max(mid+1-0, n-beg)