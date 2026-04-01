class Solution {
    public boolean hasDuplicate(int[] nums) {

       Set<Integer> mpp = new HashSet<>();

       for(int element: nums)
       {

        if(mpp.contains(element))
        {   
            return true;
        }
            mpp.add(element);
       }
    return false;
    }

}
