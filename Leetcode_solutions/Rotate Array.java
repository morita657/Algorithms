class Solution {
    public void rotate(int[] nums, int k) {
        int temp, pre;
        for(int i=0; i<k; i++){
            pre = nums[nums.length-1];
            for(int j=0;j<nums.length;j++){
                temp=nums[j];
                nums[j]=pre;
                pre=temp;
            }
        }
    }
}