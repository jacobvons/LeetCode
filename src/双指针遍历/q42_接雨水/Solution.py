class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        # Going left to right
        pointer = 0
        l_to_r = []
        prev = height[pointer]
        l_to_r.append(prev)
        while pointer < len(height) - 1:
            pointer += 1
            if height[pointer] > prev:
                l_to_r.append(height[pointer])
                prev = height[pointer]
            else:
                l_to_r.append(prev)
            
        # Going right to left
        r_to_l = []
        prev = height[pointer]
        r_to_l.append(prev)
        while pointer > 0:
            pointer -= 1
            if height[pointer] > prev:
                r_to_l.append(height[pointer])
                prev = height[pointer]
            else:
                r_to_l.append(prev)
        r_to_l.reverse()
        
        water = [min(l_to_r[i], r_to_l[i]) for i in range(0, len(height))]
        # Substracting building height
        water = sum([water[i] - height[i] for i in range(0, len(height))])
        return water
