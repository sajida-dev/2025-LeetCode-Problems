class Solution:
    def myAtoi(self, s: str) -> int:
        
        MIN = (-2)**31
        MAX = 2**31
        s = s.strip(" ")
        print(s)
        if(len(s)==0):
            return 0
        neg = False
        if(s[0] == '-'):
            neg = True
        if(s[0] == '-' or s[0] == '+'):
            s = s[1:]
        ans = 0
        
        for val in s:  
            if(val.isdigit()):
                ans = (ans*10)+int(val)
            else:
                break
        if neg:
            ans = ans*-1
        if(ans < MIN):
            return (MIN)
        elif(ans>(MAX-1)):
            return MAX-1
        return ans
        