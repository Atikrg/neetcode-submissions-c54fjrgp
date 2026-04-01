
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> st = new HashSet<>();

        for(int element: nums){

            if(st.contains(element)){
                return true;
            }
            st.add(element);
        }

        return false;


 
    }
}
