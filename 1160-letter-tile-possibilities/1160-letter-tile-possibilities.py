from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        dic = {}
        self.ans = 0
        def rec(s,per):
            if(not s):
                for perm in permutations(per):
                    dic["".join(perm)] = True
                return
            rec(s[1:],per+[s[0]])
            rec(s[1:],per)
        rec(tiles,[])
        return len(dic)-1