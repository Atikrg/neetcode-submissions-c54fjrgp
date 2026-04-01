class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> st = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int morenumbers = target - num;
            
            if (st.containsKey(morenumbers)) {
                return new int[]{st.get(morenumbers), i};
            }
            
            st.put(num, i);
        }

        return new int[]{-1, -1};
    }
}

