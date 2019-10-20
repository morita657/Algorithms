class Solution {
    public int findLength(int[] A, int[] B) {
        int ans = 0;
        int[][] memo = new int[A.length + 1][B.length + 1];
        for (int i = A.length - 1; i >= 0; i--) {
            // for (int i = 0; i <A.length ;++i) {
            for (int j = B.length - 1; j >= 0; j--) {
                // for (int j = 0; j <B.length ;++j) {
                if (A[i] == B[j]) {
                    memo[i][j] = memo[i + 1][j + 1] + 1;
                    // System.out.println(Arrays.toString(memo));
                    // System.out.println(Arrays.deepToString(memo));
                    // if (ans < memo[i][j]) ans = memo[i][j];
                    ans = Math.max(ans, memo[i][j]);
                }
            }
        }
        return ans;
    }
}