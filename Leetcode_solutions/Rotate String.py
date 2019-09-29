class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) == 0 and len(B) == 0:
            return True
        if len(A) == 0 and len(B) == 0:
            return False
        flag = False
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                flag = True
                break
        return flag
