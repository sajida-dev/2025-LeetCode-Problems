import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        temp = re.search(p,s)
        if temp and temp[0] == s:
            return True
        return False