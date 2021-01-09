class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half_inverted = 0
        while x > half_inverted:
            half_inverted = half_inverted * 10 + x % 10
            x = x // 10
        return half_inverted == x or half_inverted // 10 == x
