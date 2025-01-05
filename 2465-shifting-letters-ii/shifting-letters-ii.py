class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ar = [0]*(n+1)
        for start,end,direction in shifts:
            if(direction == 0):
                direction = -1
            ar[start] += direction
            if(end+1 < n):
                ar[end+1] -= direction
        print(ar)
        ans = ""
        sumVal = 0
        for i in range(n):
            sumVal += ar[i]
            ans += alpha[(ord(s[i])-ord('a')+sumVal)%26]
        return ans