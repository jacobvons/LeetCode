class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        left_max = 0
        right_max = 0
        l, r = 0, len(height)-1
        ans = []
        while l != r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans.append(left_max - height[l])
                l += 1
                
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans.append(right_max - height[r])
                r -= 1
                
        return sum(ans)
