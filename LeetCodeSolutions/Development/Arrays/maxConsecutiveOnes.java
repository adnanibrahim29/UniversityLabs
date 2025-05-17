class maxConsecutiveOnes {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ones = 0;
        int currentCount = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1){
                currentCount++;
                ones = Math.max(ones, currentCount);
            }else{
                currentCount = 0;
            }
        }
        return ones;
    }
}