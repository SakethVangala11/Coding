class Solution {
    public int sumOfDigits(int num){
        int sum = 0;
        while(num > 0){
            int rem = num%10;
            sum+=rem;
            num/=10;
        }
        return sum;
    }
    public int countBalls(int lowLimit, int highLimit) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = lowLimit; i <= highLimit; i++){
            int sum = sumOfDigits(i);
            map.put(sum, map.getOrDefault(sum,0)+1);
        }
        int res = 0;
        for(Map.Entry<Integer,Integer> entry: map.entrySet()){
            int val = entry.getValue();
            res = Math.max(res, val);
        }
        return res;
    }
}