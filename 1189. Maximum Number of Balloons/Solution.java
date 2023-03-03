import java.util.*;

class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> freq = new HashMap();
        text = text.toLowerCase();
        freq.put('b',0);
        freq.put('a',0);
        freq.put('l',0);
        freq.put('o',0);
        freq.put('n',0);
        for(int i = 0; i<text.length(); i++){
            if(freq.containsKey(text.charAt(i))){
                freq.put(text.charAt(i), freq.get(text.charAt(i)) + 1);
            }
        }
        System.out.println("Map" + freq);
       freq.put('l', freq.get('l')/2);
       freq.put('o', freq.get('o')/2);
       
       return Math.min(freq.get('n'), Math.min(freq.get('a'), Math.min(freq.get('b'), 
            Math.min(freq.get('l'), freq.get('o')))));
    }
}