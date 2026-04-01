class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false;

        const char_counts = new Array(26).fill(0);


        for(let i = 0; i < s.length; i++)
        {
            char_counts[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            char_counts[t.charCodeAt(i)-'a'.charCodeAt(0)]--;
        }


        for(let count of char_counts)
        {
            if(count!== 0)
            {
                return false;
            }
        }
        return true;
    }
}
