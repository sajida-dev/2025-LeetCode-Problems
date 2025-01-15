class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        setCount = bin(num2)[2:].count('1')
        co1 = list(bin(num1)[2:])
        setCount -= co1.count('1')
        if(setCount > 0):
            if(co1.count('1') != len(co1)):
                j = len(co1)-1
                while(setCount > 0):
                    if(co1[j]=='0'):
                        co1[j] = '1'
                        setCount -=1
                    j -= 1
        elif(setCount < 0):
            j = len(co1)-1
            while(setCount != 0):
                if(co1[j] == '1'):
                    co1[j] = '0'
                    setCount += 1
                j -= 1
        if(setCount > 0):
            while(setCount >0):
                co1.append('1')
                setCount -= 1
        return int("".join(co1),2)
        
       
        