class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char_no = 0
        result = ""
        for i in range(len(strs[0])):
            character = strs[0][char_no] 
            for word in strs:
        
                if(char_no >= len(word) or character != word[char_no]):
                    return result
            result += character
            char_no += 1
        return result

# res = "fl"

# char_no = 0
# character = f
# flower -> f true
# flow -> f true
# flight -> f true
# res += f
# char_no +=1 

# char_no = 1
# character = l
# flower -> l true
# flow -> l true
# flight -> l true

# char_no =2
# character = o
# flower => o true
# flow -> o true 
# flight -> i

