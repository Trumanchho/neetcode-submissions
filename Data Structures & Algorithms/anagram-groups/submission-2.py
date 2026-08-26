from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            letter_list = [0]*26
            for c in s:
                letter_list[ord(c)-ord('a')] += 1
            hmap[tuple(letter_list)].append(s)
        result = []
        for val in hmap.values():
            result.append(val)
        return result
"""
act: {a,c,t}
pots: 
"""