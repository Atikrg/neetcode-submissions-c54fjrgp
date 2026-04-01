

class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0, r = 0;
        int maxFreq = 0, maxLen = 0;
        Map<Character, Integer> hash = new HashMap<>();

        while (r < s.length()) {
            char currentChar = s.charAt(r);
            hash.put(currentChar, hash.getOrDefault(currentChar, 0) + 1);
            maxFreq = Math.max(maxFreq, hash.get(currentChar));

            // If the window size minus the max frequency is greater than k, shrink the window
            if ((r - l + 1) - maxFreq > k) {
                char leftChar = s.charAt(l);
                hash.put(leftChar, hash.get(leftChar) - 1);
                l++;
            }

            // Calculate the maximum length of the window
            maxLen = Math.max(maxLen, r - l + 1);
            r++;
        }

        return maxLen;
    }
}

