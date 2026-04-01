class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0; // Maximum profit
        int minPrice = Integer.MAX_VALUE; // Minimum price seen so far

        for (int price : prices) {
            // Update the minimum price if a lower price is found
            if (price < minPrice) {
                minPrice = price;
            } else {
                // Calculate potential profit and update maxProfit if it's greater
                maxProfit = Math.max(maxProfit, price - minPrice);
            }
        }

        return maxProfit;
    }
}
