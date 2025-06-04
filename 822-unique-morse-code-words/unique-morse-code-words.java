class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] list = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        HashSet<String> set = new HashSet<String>();
        for(String word: words) {
            StringBuilder morse = new StringBuilder();
            for(char c: word.toCharArray()){
                morse.append(list[(int)c - 97]);
            }
            set.add(morse.toString());
        }
        return set.size();
    }
}