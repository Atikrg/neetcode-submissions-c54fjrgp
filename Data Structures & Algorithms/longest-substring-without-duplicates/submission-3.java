class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Convert string to character array
        char[] charArray = s.toCharArray();

        int n = charArray.length;
        int l = 0;
        int r = 0;

        int len = 0;
        int maxlen = 0;

        // Initialize the hash map with size 256 values set to -1
        Map<Character, Integer> hash = new HashMap<>();
        for (int i = 0; i < 256; i++) {
            hash.put((char) i, -1);
        }

        while (r < n) {
            char currentChar = charArray[r];
            if (hash.get(currentChar) != -1 && hash.get(currentChar) >= l) {
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
