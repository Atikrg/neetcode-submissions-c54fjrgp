class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0; int r = 0;
        int maxFreq = 0;
        int maxLen = 0;
        int len = 0;


        Map<Character, Integer> hash = new HashMap<>();

        while(r < s.length())
        {
            len = r - l + 1;
            char currentChar = s.charAt(r);
            hash.put(currentChar, hash.getOrDefault(currentChar, 0) + 1);
            maxFreq = Math.max(maxFreq, hash.get(currentChar));
            
            if(len - maxFreq > k)
            {
                char leftChar = s.charAt(l);
                hash.put(leftChar, hash.get(leftChar) - 1);
                l++;
            }

          maxLen = Math.max(maxLen, r - l + 1);
            r++;

        }

        return maxLen;
    }
}
