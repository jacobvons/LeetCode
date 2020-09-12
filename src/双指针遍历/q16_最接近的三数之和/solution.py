class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return []
        diff = float("inf")
        nums.sort()
        for i in range(0, len(nums)-2):
            l = i + 1
            r = len(nums) -1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                new_diff = target - sum
                if new_diff == 0:
                    return target
                if abs(new_diff) < abs(diff):
                    diff = new_diff
                if sum < target:
                    l += 1
                else:
                    r -= 1
        return target - diff
