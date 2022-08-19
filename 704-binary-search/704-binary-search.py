class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start != end:
            pivot = start + (end - start) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                start = pivot + 1
            else:
                end = pivot
        return -1
            