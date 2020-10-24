public class Solution {
    public int MaxProfit(int[] prices) {
        int length = prices.Length;
        int pLeft = 0, pRight = 0;
        int maxProfit = 0;
        while (pRight < length) {
            int buyPrice = prices[pLeft];
            int sellPrice = prices[pRight];
            if (sellPrice > buyPrice) {
                maxProfit = Math.Max(sellPrice - buyPrice, maxProfit);
                pRight++;
            } else if (sellPrice < buyPrice) {
                pLeft = pRight;
                pRight++;
            } else {
                pRight++;
            }
        }
        return maxProfit;
    }
}
