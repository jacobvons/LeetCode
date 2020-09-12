class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_end = 0
        r_end = len(height)-1
        max_volume = (r_end-l_end) * min(height[r_end], height[l_end])
        while l_end != r_end:
            if height[l_end] < height[r_end]:
                l_end += 1
            else:
                r_end -= 1
            volume = (r_end-l_end) * min(height[r_end], height[l_end])
            max_volume = volume if max_volume < volume else max_volume
        return max_volume

