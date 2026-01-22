class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pal = 0
        actual = x
        while(x > 0):
            mod = x % 10 # 5
            x = x // 10 # 1234
            pal = pal * 10 + mod 
        if(actual == pal):
            return True
        return False 


        # 0 * 10 + 5 = 5
        # 5 * 10 + 4 = 54
        # 54 * 10 + 3 = 543
        # 543 * 10 + 2 = 5432
        # 5432 * 10 + 1 = 54321

        # print(test // 10)
        # print(test % 10)
        # test = test // 10
        # print(test // 10)
        # print(test % 10)
        # test = test // 10
        # print(test // 10)
        # print(test % 10)
        # return False



