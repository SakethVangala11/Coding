class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] freq = new int[n];
        int[] result = new int[n];
        int count = 0;
        for(int i = 0; i<n; i++) {
            freq[A[i]-1]+=1;
            if(freq[A[i]-1] == 2){
                count+=1;
                result[i] = count;
            }
            freq[B[i]-1]+=1;
            if(freq[B[i]-1] == 2){
                count+=1;
                result[i] = count;
            }
            result[i] = count;
        }
        return result;
    }
}