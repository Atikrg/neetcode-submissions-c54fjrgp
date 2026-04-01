class Solution {
    public int[] countBits(int n) {
           
       int[] mem = new int[n + 1];
       mem[0] = 0;
       for(int i = 1; i <= n; i++ )
       {
        mem[i] = mem[i / 2] + i % 2;
       }
       return mem;
    }
}
