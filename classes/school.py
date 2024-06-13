from classes.staff import Staff
from classes.student import Student

class School:

    @staticmethod
    def add_student(student_data):
        Student.student_list.append(Student(**student_data))
    
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        #Loop through just CSV added students 
        '''for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')'''
        for i, student in enumerate(Student.student_list):
            print(f'{i + 1}.{student.name} | {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in Student.student_list:
            if student.school_id == student_id:
                print('\n')
                print(f""" Name: {student.name} | ID: {student.school_id}  """)


    