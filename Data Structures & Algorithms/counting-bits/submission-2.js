class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
        const arr = new Array(n+1).fill(0);

        for(let i = 0; i <=n; i++)
        {
            arr[i] = arr[Math.floor(i / 2)] + i %2;

        }

    

        return arr;
    }
}
