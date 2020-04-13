class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in arr:
                count += 1
        return count