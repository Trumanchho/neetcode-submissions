class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] # [i,t]
        for i, t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                p_i, p_t = stack.pop()
                res[p_i] = i - p_i
            stack.append((i,t))
        return res

                
"""
[38 36 35] 40
 1  3  4   5 
"""