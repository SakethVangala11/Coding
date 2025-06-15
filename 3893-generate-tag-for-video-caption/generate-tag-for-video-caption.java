class Solution {
    public String generateTag(String caption) {
        StringBuilder result  = new StringBuilder("#");
        Boolean flag = false;
        Boolean firstChar = true;
        for(char ch: caption.toCharArray()) {
            if(ch == ' '){
                flag = true;
                continue;
            }
            if(firstChar) {
                result.append(Character.toLowerCase(ch));
                firstChar = false;
                flag =  false;
                continue;
            }
            if(flag == true) {
                result.append(Character.toUpperCase(ch));
                flag = false;
            }else{
                result.append(Character.toLowerCase(ch));
            }
            if(result.length() == 100) {
                break;
            }
        }
        return result.toString();
    }
}