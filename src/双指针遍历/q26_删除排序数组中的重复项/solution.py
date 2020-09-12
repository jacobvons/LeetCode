class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        l = 0
        r = 1
        while r != len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
                r += 1
        return l + 1
