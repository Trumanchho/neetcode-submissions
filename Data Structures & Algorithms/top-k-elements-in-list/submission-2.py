from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for key in hmap.keys():
            buckets[hmap[key]].append(key)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res



        # {
        #     1: 1
        #     2: 2
        #     3: 3
        # }