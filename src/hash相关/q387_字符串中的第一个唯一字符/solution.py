class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        indices = [s.index(char) for char in alphabet if s.count(char)==1]
        return min(indices) if len(indices)!=0 else -1
