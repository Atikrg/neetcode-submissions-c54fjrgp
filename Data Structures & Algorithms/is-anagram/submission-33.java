class Solution {
    public boolean isAnagram(String s, String t) {
        Set<Integer> set = new HashSet<>();

        if(s.length() != t.length()) return false;

        int[] char_counts = new int[26];


        for(int i = 0; i < s.length(); i++)
        {
            char_counts[s.charAt(i) - 'a']++;
            char_counts[t.charAt(i) - 'a']--;
        }

        for(int num: char_counts){
            if(num != 0){
                return false;
            }
        }
        return true;
    } 
}
