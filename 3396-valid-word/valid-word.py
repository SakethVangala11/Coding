class Solution:
    def isValid(self, word: str) -> bool:
        minChar, conditionTwo, vowel, consonant = False, False, False, False
        if len(word) >=3:
            minChar = True
        if '@' in word or '#' in word or '$' in word:
            return False
        for i in word:
            if (ord(i) >=48 and ord(i)<=57) or (ord(i) >=65 and ord(i)<=90) or (ord(i) >=97 and ord(i)<=122):
                conditionTwo = True
            if i in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']:
                vowel = True
            if ((ord(i) >=65 and ord(i)<=90) or (ord(i) >=97 and ord(i)<=122)) and i not in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']:
                consonant = True
        print(minChar, conditionTwo, vowel, consonant)
        return  minChar and conditionTwo and vowel and consonant
        

        