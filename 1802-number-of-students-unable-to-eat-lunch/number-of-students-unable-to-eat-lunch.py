class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        count = 0
        while(students and count != n):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                n = len(students)
                count = 0
            else:
                x = students.pop(0)
                students.append(x)
                count+=1
            
        if not students:
            return 0
        return len(students)
            
        