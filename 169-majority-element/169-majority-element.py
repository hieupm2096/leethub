class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # numsMap = {}
        # for i in nums:
        #     if i in numsMap:
        #         numsMap[i] += 1
        #     else:
        #         numsMap[i] = 1
        # maxEntry = [0, 0]
        # for k, v in numsMap.items():
        #     if v > maxEntry[1]:
        #         maxEntry = [k, v]
        # return maxEntry[0]
        nums.sort()
        return nums[len(nums) // 2]