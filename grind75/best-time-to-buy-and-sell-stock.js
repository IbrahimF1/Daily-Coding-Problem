// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let min = 10**4

    for (i of prices){
        min = Math.min(i, min)
        profit = Math.max(profit, i-min)
    }

    return profit
};
