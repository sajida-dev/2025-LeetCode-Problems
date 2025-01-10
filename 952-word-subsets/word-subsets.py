import copy
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2 = list(set(words2))
        words2.sort(reverse=True,key=len)
        dic = {}
        for word in words2:
            temp = {}
            for w in word:
                if w not in temp:
                    temp[w] = 1
                else:
                    temp[w] += 1
            for k in temp.keys():
                if k in dic:
                    dic[k] = max(dic[k],temp[k])
                else:
                    dic[k] = temp[k]
        ans = []
        for word in words1:
            tmp = {}
            for a in word:
                if a in tmp:
                    tmp[a] += 1
                else:
                    tmp[a] = 1
            for k in dic.keys():
                if k in tmp:
                    if tmp[k] < dic[k]:
                        is_universal = False
                        break
                else:
                    is_universal = False
                    break
            else:
                ans.append(word)
        return ans
