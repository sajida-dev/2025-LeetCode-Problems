class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        dic  = {}
        ans = [0]*n
        for i in range(n):
            if(boxes[i] == '1'):
                dic[i] = True
        for i in range(n):
            for key in dic.keys():
                if(i != key):
                    ans[i] += abs(key-i)
                #print(ans)
        return ans