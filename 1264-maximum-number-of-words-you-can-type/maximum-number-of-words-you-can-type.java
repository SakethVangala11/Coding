class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {
        String[] words = text.split(" ");
        HashSet<Character> broken = new HashSet<Character>();
        int res = 0;
        for(int i = 0; i<brokenLetters.length(); i++){
            broken.add(brokenLetters.charAt(i));
        }
        for(String word: words){
            int n = word.length();
            boolean flag = true;
            for(int i = 0; i < n; i++){
                if(broken.contains(word.charAt(i))){
                    flag = false;
                    break;
                }
            }
            if(flag == true){
                res+=1;
            }
        }
        return res;
    }
}