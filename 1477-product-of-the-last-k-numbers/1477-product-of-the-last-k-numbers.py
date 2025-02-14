class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.pre = []
        self.isZero = -1
    def add(self, num: int) -> None:
        if(num == 0):
            self.isZero = len(self.nums)
        self.nums.append(num)
        if(self.pre and self.pre[-1]!=0):
            self.pre.append(self.pre[-1]*num)
        else:
            self.pre.append(num)

    def getProduct(self, k: int) -> int:
        start = len(self.nums) - k 
        if(start <= self.isZero < len(self.nums)):
            return 0
        if(len(self.nums) == k):
            return self.pre[-1]
        if(self.nums[-1*(k+1)] != 0):
            return self.pre[-1]//self.pre[-1*(k+1)]
        else:
            return self.pre[-1]
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
