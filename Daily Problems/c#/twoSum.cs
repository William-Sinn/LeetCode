public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int i = 0;
        int j; 
        
        foreach (int num in nums) {
            j = 0;
            foreach (var num2 in nums) {
                if (i == j) {}
                else if (num + num2 == target) {
                    return [i, j];
                } 
                j++;
            }
            i++;
        }
        return [];
    }
}