class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowel(s):
            val = s[0]
            if(val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u'):
                val = s[-1]
                if(val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u'):
                    return True
            return False
        n = len(words)
        vowelCheck = [0]*n
        for i in range(n):
            if isVowel(words[i]):
                vowelCheck[i] = 1
        # [1,0,1,1,1]
        n = len(queries)
        ans = [0]*n
        for i in range(n):
            left,right = queries[i]
            ans[i] = vowelCheck[left:right+1].count(1)
        return ans
