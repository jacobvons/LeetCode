class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_l = 0
        window_r = 0
        longest = 0
        window = set()
        while window_l < len(s) and window_r < len(s):
            if s[window_r] not in window:
                window.add(s[window_r])
                window_r += 1
            else:
                window.remove(s[window_l])
                window_l += 1
            window_length = window_r - window_l
            if window_length > longest:
                longest = window_length
        return longest
