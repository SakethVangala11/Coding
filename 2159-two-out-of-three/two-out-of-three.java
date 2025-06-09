class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        Map<Integer, Integer> freq = new HashMap<>();
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        Set<Integer> set3 = new HashSet<>();

        for (int n : nums1) set1.add(n);
        for (int n : nums2) set2.add(n);
        for (int n : nums3) set3.add(n);

        for (int n : set1) freq.put(n, freq.getOrDefault(n, 0) + 1);
        for (int n : set2) freq.put(n, freq.getOrDefault(n, 0) + 1);
        for (int n : set3) freq.put(n, freq.getOrDefault(n, 0) + 1);

        List<Integer> result = new ArrayList<>();
        for(Integer key: freq.keySet()) {
            if(freq.get(key) >=2) {
                result.add(key);
            }
        }
        return result;
    }
}