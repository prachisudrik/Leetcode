class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        if len(students) != 0 and len(sandwiches) != 0:
            while len(students)>0 and count != len(students):
                if students[0] == sandwiches[0]:
                    students.pop(0)
                    sandwiches.pop(0)
                    count = 0
                else:
                    popped_element = students.pop(0)
                    students.append(popped_element)
                    count = count + 1
            return len(students)

        
