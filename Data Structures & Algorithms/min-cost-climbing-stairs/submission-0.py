class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dpArr = [0] * (len(cost) + 1)

        for i in range(2, len(dpArr)):
            dpArr[i] = min(cost[i-2]+dpArr[i-2], cost[i-1]+dpArr[i-1])
    
        return dpArr[-1]





"""
[1,2,1,2,1,1,1]
[0,0,1,2,2,3,3,4]

"""
