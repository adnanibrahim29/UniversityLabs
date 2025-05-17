class removeElement {
    public int removingElement(int[] nums, int val) {
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != val){
                nums[count] = nums[i]; // Shifting elements to the right
                count++;
            }

        }
        return count;
    }
}