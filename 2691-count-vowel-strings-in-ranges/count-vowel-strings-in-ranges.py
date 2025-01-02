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
            if(i>0):
                vowelCheck[i] = vowelCheck[i]+vowelCheck[i-1]
            #print(vowelCheck)
        # [1,0,1,1,1]
        n = len(queries)
        ans = [0]*n
        for i in range(n):
            left,right = queries[i]
            if(left>0):
                ans[i] = vowelCheck[right]-vowelCheck[left-1]
            else:
                ans[i] = vowelCheck[right]
            #print(ans)
        return ans
