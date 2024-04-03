public class Solution {
    public bool IsIsomorphic(string s, string t) {

        Dictionary<char, char> char_dict = new Dictionary<char, char>{};

        if (t.Length != s.Length) {
            return false;
        }
        
        int i = 0;
        foreach (char c in s){

            if (!char_dict.ContainsKey(c)) {
                if (char_dict.ContainsValue(t[i])) {
                    return false;
                }

                char_dict[c] = t[i];
            }
            else {
                if (char_dict[c] != t[i]) {
                    return false;
                }
                
            }
            i++;
        }

        return true;
        
    }
}