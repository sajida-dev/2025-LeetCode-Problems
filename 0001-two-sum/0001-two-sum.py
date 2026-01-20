class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]


# sum = num[0] + num[1]  
# sum = num[0] + num[2]
# sum = num[0] + num[3]
# sum = num[1] + num[2]
# sum = num[1] + num[3]
# sum = num[1] + num[0]
# sum = num[2] + num[3]
# sum = 
# sum == target -- ending condition

# range()
# if single parm: end value
# if 2 parm : start value, end value
# if 3 parm : start value, end value, increment 