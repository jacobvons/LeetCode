public class Solution {
    public int cal(int n) {
        int sum = 0;
        while (n != 0) {
            sum += (int)Math.Pow(n % 10, 2);
            n /= 10;
        }
        return sum;
    }
    public bool IsHappy(int n) {
        int fast = cal(n);
        int slow = n;
        while (fast != slow) {
            if (fast == 1) {
                return true;
            }
            fast = cal(cal(fast));
            slow = cal(slow);
        }
        return fast == 1 ? true : false;
    }
    
}
