

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0; // Edge case: empty array

        Arrays.sort(nums); // Sort the array

        int longest = 1; // To track the longest sequence
        int currentLength = 1; // Length of the current sequence

        for (int i = 1; i < nums.length; i++) {
            // Skip duplicates
            if (nums[i] == nums[i - 1]) continue;

            // Check if the current number is consecutive
            if (nums[i] == nums[i - 1] + 1) {
                currentLength++; // Increment the current sequence length
            } else {
                // Reset current length
                longest = Math.max(longest, currentLength);
                currentLength = 1; // Start a new sequence
            }
        }

        // Ensure the last sequence is considered
        longest = Math.max(longest, currentLength);

        return longest;
    }
}
