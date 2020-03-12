class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = ""
        flag = False
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            current += strs[0][i]
            for j in range(len(strs)):
                if strs[j][:i + 1] == current:
                    continue
                else:
                    flag = True
                    break
            if flag:
                break
        if flag:
            return current[:-1]
        return current

# use only differences


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            # iter_target is the shortest one from two elements
            if len(prefix) < len(strs[i]):
                iter_target = prefix
                rest = strs[i]
            else:
                iter_target = strs[i]
                rest = prefix
            current = ""
            # take only common part as the prefix
            for j in range(len(iter_target)):
                if iter_target[j] == rest[j]:
                    current += rest[j]
                else:
                    prefix = current
                    break
            prefix = current
        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            candidate = strs[0][i]
            for j in range(len(strs[1:])):
                if len(strs[1+j]) < i+1:
                    return prefix
                elif strs[1+j][i] != candidate:
                    return prefix
            prefix += candidate
        return prefix
