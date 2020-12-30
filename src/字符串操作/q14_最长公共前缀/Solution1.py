class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        current_pref = strs[0]
        next_ind = 1
        while current_pref != "" and next_ind < len(strs):
            next_str = strs[next_ind]
            next_pref = ""
            for i in range(0, min(len(current_pref), len(next_str))):
                if current_pref[i] == next_str[i]:
                    next_pref += next_str[i]
                else:
                    break
            current_pref = next_pref
            next_ind += 1
        return current_pref
