class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Store all nums in hashset
        map = {}
        for i, num in enumerate(nums):
            map[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in map and i != map[diff]:
                return [i,map[diff]]
        return []

        