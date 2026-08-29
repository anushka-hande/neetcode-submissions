class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sorted_s = s.toCharArray();
        char[] sorted_t = t.toCharArray();
        

        if (s.length() == t.length()){
            Arrays.sort(sorted_s);
            Arrays.sort(sorted_t);
            return Arrays.equals(sorted_s, sorted_t);
        }
        else{
            return false;
        }
    }
}
