from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums
        d = defaultdict(lambda: 0)
        for i in nums:
            d[i] += 1
        bucket = [None] * (len(nums) + 1)
        for key, value in d.items():
            if not bucket[value]:
                bucket[value] = []
            bucket[value].append(key)
        rs = []
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            if len(rs) < k:
                rs += bucket[i]
            else:
                break
        return rs[:k]
            