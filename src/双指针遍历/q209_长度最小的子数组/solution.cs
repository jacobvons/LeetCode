public class Solution {
    public int MinSubArrayLen(int s, int[] nums) {
        if (nums.Length == 0 || nums.Sum() < s) {
            return 0;
        } else if (nums.Sum() == s) {
            return nums.Length;
        }
        
        int sum = 0;
        int pLeft = 0;
        int result = Int32.MaxValue;
        for (int pCurrent = 0; pCurrent < nums.Length; pCurrent ++) {
            sum += nums[pCurrent];
            while (sum >= s) {
                result = Math.Min(result, pCurrent - pLeft + 1);
                sum -= nums[pLeft];
                pLeft ++;
            }
        }
        return result;
    }
}
