
class Solution {
    public String minWindow(String s, String t) {
        int l = 0;
        int r = 0;
        int n = s.length();
        int m = t.length();
        int startIndex = -1;
        int minLen = Integer.MAX_VALUE;
        int count = 0;

        // Create the frequency map from string t
        HashMap<Character, Integer> freqMap = new HashMap<>();
        for (int i = 0; i < m; i++) {
            char ch = t.charAt(i);
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }

        // Track the number of characters from t in the current window
        int requiredCount = m;

        while (r < n) {
            char currentChar = s.charAt(r);

            // If the current character is in t, decrease its frequency in freqMap
            if (freqMap.containsKey(currentChar)) {
                freqMap.put(currentChar, freqMap.get(currentChar) - 1);
                if (freqMap.get(currentChar) >= 0) {
                    count++;
                }
            }

            // Try to minimize the window when all characters from t are present in the window
            while (count == requiredCount) {
                if ((r - l + 1) < minLen) {
                    minLen = r - l + 1;
                    startIndex = l;
                }

                char leftChar = s.charAt(l);
                if (freqMap.containsKey(leftChar)) {
                    freqMap.put(leftChar, freqMap.get(leftChar) + 1);
                    if (freqMap.get(leftChar) > 0) {
                        count--;
                    }
                }
                l++;
            }

            r++;
        }

        // Return the smallest window or an empty string if no such window exists
        return startIndex == -1 ? "" : s.substring(startIndex, startIndex + minLen);
    }
}
