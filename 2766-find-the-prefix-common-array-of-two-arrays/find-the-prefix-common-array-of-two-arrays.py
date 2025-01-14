class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0]*n
        count = 0
        fre = {}
        for i in range(n):
            if A[i] not in fre:
                fre[A[i]] = 1
            else:
                count += 1
                fre.pop(A[i])
            if B[i] not in fre:
                fre[B[i]] = 1
            else:
                count += 1
                fre.pop(B[i])
            #print(fre)
            ans[i] = count
        return ans