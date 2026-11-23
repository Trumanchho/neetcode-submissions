class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]

        if n <= 2: return dp[n-1]

        i = 2
        while i<n:
            dp.append(dp[i-1]+dp[i-2])
            i += 1
        return dp[n-1]

"""    
    1 2 3 4   5  
    1 2 2+1 3+2 5+3

    11111
    2111
    1211
    1121
    1112
    221
    122
    212
"""