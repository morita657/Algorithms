class Solution {
    public void reverseString(char[] s) {
        int len = 0;
        if (s.length % 2 == 0) {
            len = s.length / 2;
        } else {
            len = s.length / 2 + 1;
        }
        int last = s.length - 1;
        for (int i = 0; i < len; i++) {
            char temp = s[last];
            s[last] = s[i];
            s[i] = temp;
            last--;
        }
    }
}
