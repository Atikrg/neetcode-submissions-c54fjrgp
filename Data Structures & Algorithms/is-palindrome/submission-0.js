class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const cleaned_str = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

        let i = 0;
        let j = cleaned_str.length - 1;

        while(i < j)
        {
            if(cleaned_str[i] !== cleaned_str[j])
            {
                return false;
            }
                i++;
                j--;
        }

        return true;



    }
}
