from queue import PriorityQueue 
class Solution:
    def minOperations(self, q: List[int], k: int) -> int:
        p = PriorityQueue()
        ans = 0
        for val in q:
            p.put(val)        
        while(p.qsize() >= 2):
            x,y = p.get(),p.get()
            if(x >= k):
                break
            p.put((x*2)+y)
            ans += 1
        return ans        