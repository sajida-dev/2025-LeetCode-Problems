class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        fre = [0]*n
        ans = [0]*n
        count = 0
        for i in range(n):
            fre[A[i]-1] += 1
            fre[B[i]-1] += 1
            if(fre[A[i]-1] == 2):
                count += 1
                fre[A[i]-1] = 0
            if(fre[B[i]-1] == 2):
                count += 1
                fre[B[i]-1] = 0
            ans[i] = count
        return ans