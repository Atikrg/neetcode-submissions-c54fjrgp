class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 1;
        int count = 0;
        int lastSmaller =  Integer.MIN_VALUE;;

        if(nums.length == 0) return 0;
        Arrays.sort(nums);

         // Find the longest consecutive sequence
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] - 1 == lastSmaller) {
                // a[i] is the next element in the current sequence
                count += 1;
                lastSmaller = nums[i];
            } else if (nums[i] != lastSmaller) {
                // Reset the sequence if there's a gap
                count = 1;
                lastSmaller = nums[i];
            }
            // Update the longest sequence found
            longest = Math.max(longest, count);
        }
        return longest;
    }
}
