class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for ind_i, i in enumerate(words):
            for ind_j, j in enumerate(words):
                if i != j and j in i:
                    res.add(j)
        return list(res)