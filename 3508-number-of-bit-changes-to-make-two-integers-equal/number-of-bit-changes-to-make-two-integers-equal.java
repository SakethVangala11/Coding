class Solution {
    public int minChanges(int n, int k) {
        int changes = 0;
        for(int i = 0; i < 32;i++){
           if((n & 1<<i) > 0  && (k & 1<<i) == 0){
                changes+=1;
           }else if((n & 1<<i) == 0 && (k & 1<<i) > 0){
            return -1;
           }
        }

        return changes;
        
    }
}