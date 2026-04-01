class Solution {
    public int longestConsecutive(int[] nums) {
        int longestLength = 0;

        Map<Integer, Boolean> exploredMap = new HashMap<>();

        for(int num: nums)
        {
            exploredMap.put(num, Boolean.FALSE);
        }


        for(int num: nums)
        {
            int currentLength = 1;
            
            //move forward
            int nextNum = num + 1;
            while(exploredMap.containsKey(nextNum) && exploredMap.get(nextNum) == false)
            {
                currentLength += 1;
                exploredMap.put(nextNum, Boolean.TRUE);
                nextNum += 1;
            }
            
            //move previous
            int prevNum = num - 1;

            while(exploredMap.containsKey(prevNum) && exploredMap.get(prevNum) == false)
            {
                currentLength += 1;
                exploredMap.put(prevNum, Boolean.TRUE);
                prevNum -= 1;
            }

            longestLength = Math.max(longestLength, currentLength);

            
        }
            return longestLength;
    }
}
