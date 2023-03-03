class Solution {
    public int strStr(String haystack, String needle) {
        int needlePtr = 0;
        int startIdx = -1;
        if(haystack.length() < needle.length()){
            return -1;
        } else if(haystack.length() == needle.length() && haystack.equals(needle)){
            return 0;
        }
        for(int i = 0; i<haystack.length() - needle.length() + 1; i++){
            System.out.println(haystack.substring(i, i + needle.length()));
            if(haystack.substring(i, i + needle.length()).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}