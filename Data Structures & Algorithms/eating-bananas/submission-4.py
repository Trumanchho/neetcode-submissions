import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        res = 0
        while min_k <= max_k:
            time = 0
            k = (max_k + min_k) // 2
            for pile in piles:
                time += math.ceil(pile/k)
            if time > h: # k is too small!
                min_k = k + 1
            if time <= h:
                res = k
                max_k = k - 1
        return res
"""
1, 4, 3, 2
   
"""