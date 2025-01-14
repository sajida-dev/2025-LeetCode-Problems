class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        fre = [0]*n
        ans = [0]*n
        for i in range(n):
            fre[A[i]-1] += 1
            fre[B[i]-1] += 1
            #print(fre)
            ans[i] = fre.count(2)
            #print(ans)
        return ans