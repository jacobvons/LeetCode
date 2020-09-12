class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]
