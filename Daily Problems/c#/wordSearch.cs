public class Solution {
    public bool Exist(char[][] board, string word) {
        int i = 0;
        int j = 0;

        while (i <= word.Length & j <= word.Length) {
            if (word[i] == board[i][j])
            j++; 
        }

        return false;
    }
}