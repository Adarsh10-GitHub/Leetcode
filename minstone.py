from math import floor
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        sum=0
        while(k>0):
            max=0
            for i in piles:
                if(piles[i]>piles[max]):
                    max=i
            piles[max]=floor(piles[max]/2)
        k=k-1
        for i in piles:
            sum+=piles[i]
        return sum