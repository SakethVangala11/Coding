class Solution {
    public int countWords(String[] words1, String[] words2) {
        int n1 = words1.length;
        int n2 = words2.length;
        HashMap<String, Integer> w1 = new HashMap<String, Integer>(); 
        HashMap<String, Integer> w2 = new HashMap<String, Integer>(); 

        for(int i=0;i<n1;i++){
            if(w1.get(words1[i])!=null){
                w1.put(words1[i], w1.get(words1[i])+1);
            }else{
                w1.put(words1[i], 1);
            }
        }
        for(int i=0;i<n2;i++){
            if(w2.get(words2[i])!=null){
                w2.put(words2[i], w2.get(words2[i])+1);
            }else{
                w2.put(words2[i], 1);
            }
        }

        System.out.println(w1);
        System.out.println(w2);

        int count;
        count = 0;

        for(Map.Entry<String, Integer> set : w1.entrySet()){
            if(set.getValue()==1 && w2.get(set.getKey())!=null && w2.get(set.getKey())==1){
                count+=1;
            }
        }
        

        return count;
    }
}