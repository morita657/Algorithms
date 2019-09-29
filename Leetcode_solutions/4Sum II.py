class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        output = collections.defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                output[A[i] + B[j]] += 1

        for k in range(len(C)):
            for l in range(len(D)):
                ans += output[-C[k] - D[l]]
        return ans
