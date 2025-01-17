import copy
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n=len(derived)
        xor = 0
        for i in range(n):
            xor ^= derived[i]
        if(xor):
            return False
        return True