class Solution {
    isAnagram(s, t) {
        // If lengths don't match, they can't be anagrams
        if (s.length !== t.length) return false;

        // Create an array to store character counts (26 letters for 'a' to 'z')
        const char_counts = new Array(26).fill(0);

        // Loop through both strings simultaneously
        for (let i = 0; i < s.length; i++) {
            char_counts[s.charCodeAt(i) - 'a'.charCodeAt(0)]++; // Increment count for s
            char_counts[t.charCodeAt(i) - 'a'.charCodeAt(0)]--; // Decrement count for t
        }

        // Check if all counts are zero
        for (let count of char_counts) {
            if (count !== 0) {
                return false;
            }
        }

        return true; // All counts are zero, meaning s and t are anagrams
    }
}
