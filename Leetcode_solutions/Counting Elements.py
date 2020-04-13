class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in arr:
                count += 1
        return count

class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in hash_set:
                count += 1
        return count