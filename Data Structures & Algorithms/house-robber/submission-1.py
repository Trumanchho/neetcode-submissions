class Solution:
    def rob(self, nums: List[int]) -> int:
        dparr = [0] * len(nums)
        total_max = 0
        prev_max = 0
        for i in range(len(nums)):
            if i-2 < 0:
                dparr[i] = nums[i]
                #curr_amt = nums[i]
            else:
                prev_max = max(dparr[i-2], prev_max)
                dparr[i] = nums[i] + prev_max
                #t = nums[i] + dparr[i-2]
            total_max = max(dparr[i], total_max)

        return total_max

"""
tm = 15
pm = 12
[2,9,8, 3, 1  3  1  1]
[2 9 10 12 11 15 13]
"""