class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let mini = prices[0];
        let profit = 0;
        let cost = 0;

        for(let i = 0; i < prices.length; i++)
        {
            cost = prices[i] - mini;
            profit = Math.max(profit, cost);
            mini = Math.min(mini, prices[i]);
        }
        return profit;

    }
}
