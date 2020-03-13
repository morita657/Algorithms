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

# Vertical scanning
# Time complexity: O(S) where S is the sum of all characters
# Space complexity: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0: i]
        return strs[0]

# Divide and Couquer
# Time complexity: O(S) where S is the number of all characters in the array, S = m*n
# Space complexity: O(m*log n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        return self._longestCommonPrefix(strs, 0, len(strs) - 1)
        
    def _longestCommonPrefix(self, strs, l, r):
        if l == r:
            return strs[l]
        else:
            mid = (l + r) // 2
            lcpLeft = self._longestCommonPrefix(strs, l, mid)
            lcpRight = self._longestCommonPrefix(strs, mid + 1, r)
            return self.commonPrefix(lcpLeft, lcpRight)
    
    def commonPrefix(self, left, right):
        mini = min(len(left), len(right))
        for i in range(mini):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:mini]

# Binary Search
# Time complexity: O(S * log N) where S is the sum of all characters in all strings
# Space complexity: O(1)

import sys
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        minLen = sys.maxsize
        for string in range(len(strs)):
            minLen = min(minLen, len(strs[string]))
        low = 0
        high = minLen
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        print(low, high)
        return strs[0][0: (low + high) // 2]
    
    def isCommonPrefix(self, strs, length):
        str1 = strs[0][0:length]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True