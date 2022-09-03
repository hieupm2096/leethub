from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d is a hashmap(referred as dictionary in python)
        d = defaultdict(lambda: 0)
        for i in nums:
            d[i] += 1
        keys = list(d.keys())
        keys.sort(key=lambda x: (-d[x], x))
        return keys[0:k]
            