class Solution {
    public int lengthOfLongestSubstring(String s) {
        char charArray[] = s.toCharArray();
        int l = 0; int r = 0;
        int len = 0; int maxlen = 0;
        int n = s.length();

        HashMap<Character, Integer> hash = new HashMap<>();

        for(int i = 0; i < charArray.length; i++)
        {
            hash.put(charArray[i], -1);
        }


        while(r < n)
        {
            char currentChar = charArray[r];

            if(hash.get(currentChar) != -1 && hash.get(currentChar) >= l)
            {
                l = hash.get(currentChar) + 1;
            }

            len = r - l + 1;
            maxlen = Math.max(len, maxlen);
            hash.put(currentChar, r);
            r++;
        }
        return maxlen;
    }
}

 
