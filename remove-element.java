class Solution {
    public int removeElement(int[] nums, int val) {
        int front = 0;
        int back = nums.length;
        while (front < back) {
            if (nums[front] == val) {
                nums[front] = nums[back - 1];
                back--;
            } else {
                front++;
            }
        }
        return back;
    }
}