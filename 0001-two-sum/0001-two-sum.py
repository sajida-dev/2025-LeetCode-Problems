class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0,len(nums)):
            sub = target - nums[i]
            if sub in dic:
                return [dic[sub],i]
            else:
                dic[nums[i]] = i
            


# dic = {}
# dic['key'] =value
# {2:0,}

# 9-7 = 2
# if  2 is in dic:
#     return [dic[2],i]
# else 
#     dic[2] = index


# [3,2,4]
# 6-3 =3
# 6-2 = 4
# 6-4 = 2
# {3:0,2:1,}


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