class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        StringBuilder first = new StringBuilder("");
        StringBuilder second = new StringBuilder("");
        StringBuilder third = new StringBuilder("");
        for(char c: firstWord.toCharArray()){
            first.append(Character.forDigit((int) c -97, 10));
        }
        for(char c: secondWord.toCharArray()){
            second.append(Character.forDigit((int) c -97, 10));
        }
        for(char c: targetWord.toCharArray()){
            third.append(Character.forDigit((int) c -97, 10));
        }
        return Integer.parseInt(first.toString()) + Integer.parseInt(second.toString()) == Integer.parseInt(third.toString());
    }
}