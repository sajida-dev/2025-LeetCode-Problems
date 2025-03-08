class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        minOperation = whites
        for i in range(1, len(blocks)-k+1):
            if(blocks[i-1] != blocks[i+k-1]):
                if(blocks[i-1] == 'W'):
                    whites -= 1
                elif(blocks[i-1] == 'B'):
                    whites += 1
            minOperation = min(minOperation,whites)
        return minOperation