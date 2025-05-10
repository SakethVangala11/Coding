class Solution {
    public int maxFreqSum(String s) {
        HashMap<Character, Integer> frequency = new HashMap<Character,Integer>();
        int maxVowels = 0;
        int maxConsonants = 0;
        for(int i = 0; i<s.length(); i++) {
            frequency.put(s.charAt(i), frequency.getOrDefault(s.charAt(i),0)+1);
            int freq = frequency.get(s.charAt(i));
            if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u'){
                if(freq > maxVowels) {
                    maxVowels = freq;
                }
            } else {
                if( freq > maxConsonants) {
                    maxConsonants = freq;
                }
            } 
        }
        return maxVowels + maxConsonants;
    }
}