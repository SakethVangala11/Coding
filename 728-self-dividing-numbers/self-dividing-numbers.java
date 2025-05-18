class Solution {
    public Boolean checkIfSelfDividing(int num) {
        Boolean flag = true;
        int originalNum = num;
        while(num > 0) {
            int rem = num%10;
            if(rem == 0 || originalNum%rem != 0) {
                flag = false;
                break;
            }
            num/=10;
        }
        return flag;
    }
    public List<Integer> selfDividingNumbers(int left, int right) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = left; i<=right; i++) {
            Boolean res = checkIfSelfDividing(i);
            if(res == true) {
                list.add(i);
            }
        }
        return list;
    }
}