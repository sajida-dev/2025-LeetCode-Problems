class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        val1,val2 = 0,0
        for val in arr1:
            val1 ^= val
        for val in arr2:
            val2 ^= val
        return val1&val2