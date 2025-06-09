class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        HashSet<Integer> set1 = Arrays.stream(nums1).boxed().collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> set2 = Arrays.stream(nums2).boxed().collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> set3 = Arrays.stream(nums3).boxed().collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> result = new HashSet<Integer>();
        for(Integer element: set1){
            if(set2.contains(element) || set3.contains(element)){
                result.add(element);
            }
        }
        for(Integer element: set2){
            if(set1.contains(element) || set3.contains(element)){
                result.add(element);
            }
        }
        for(Integer element: set3){
            if(set1.contains(element) || set2.contains(element)){
                result.add(element);
            }
        }
        List<Integer> list = result.stream().collect(Collectors.toList());
        return list;
    }
}