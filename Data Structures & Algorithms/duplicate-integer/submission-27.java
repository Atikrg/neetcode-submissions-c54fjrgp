class Solution {
    public boolean hasDuplicate(int[] nums) {

     Set<Integer> set = new HashSet<>();

     for(int element: nums)
     {

        if(set.contains(element))
        {
            return true;
        }
        set.add(element);
     }

     return false;

    }
}
