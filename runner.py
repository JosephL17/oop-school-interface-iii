from classes.school import School 
from classes.student import Student

school = School('Ridgemont High') 

while True:
    mode = input("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    # List All Students
    if mode == '1':
        school.list_students()

    # View Individual Student <student_id>
    elif mode == '2':
        student_id = input('Enter student id:')
        # student_string = str(school.find_student_by_id(student_id))
        # print(student_string)
        school.find_student_by_id(student_id)

    # Add a Student
    elif mode == '3':
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        print(type(student_data))
        school.add_student(student_data)
       

    #Remove a Student <student name>
    elif mode == '4':
        delete = input('Name of student to delete: ')
        Student.student_list = [student for student in Student.student_list if student.name != delete]

    #Quit
    elif mode == '5':
        print('Exited')
        break
