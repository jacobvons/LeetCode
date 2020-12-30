class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        output = ""
        first = strs[0]
        rest = strs[1:]
        min_len = min([len(s) for s in strs])
        for i in range(0, min_len):
            current_char = first[i]
            for j in range(0, len(rest)):
                if rest[j][i] != current_char:
                    return output
            output += current_char
        return output
