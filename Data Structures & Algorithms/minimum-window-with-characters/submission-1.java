class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> freqMap = new HashMap<>();


        //populate the freqMap with t 
        for(int i = 0 ; i < t.length(); i++)
        {
            char ch = t.charAt(i);
            freqMap.put(ch, freqMap.getOrDefault(ch, 0)+1);
        }


        int uniqueCharCount = freqMap.size();
        int count = 0;
        int startIndex = -1;
        int minLen = Integer.MAX_VALUE;
        int n = s.length();
        int m = t.length();

        int windowStart = 0;

        for(int windowEnd = 0; windowEnd < n; windowEnd++)
        {
            char ch = s.charAt(windowEnd);
            if(freqMap.containsKey(ch))
            {
                freqMap.put(ch, freqMap.get(ch) - 1);

                if(freqMap.get(ch) == 0)
                {
                    uniqueCharCount--;
                }
            }
        


        while(uniqueCharCount == 0)
        {
            int len = windowEnd - windowStart + 1;
            if(len < minLen)
            {
                minLen = len;
                startIndex = windowStart;
            }


            char startChar = s.charAt(windowStart);
            if(freqMap.containsKey(startChar))
            {
                freqMap.put(startChar, freqMap.get(startChar)+1);

                if(freqMap.get(startChar) > 0)
                {
                    uniqueCharCount++;
                }
            }
            windowStart++;
        }

        }
        if(startIndex == -1)
        {
            return "";
        }

        return s.substring(startIndex, startIndex + minLen);
    } 
}
