from School import School, ClassRoom, Subject
from Persons import Student, Teacher

def main():
    school = School('Modern School', 'Patiya')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    #add Students 
    Simran = Student('Simran Rahaman', eight)
    school.student_admission(Simran)
    rafsan = Student('Rafsan Rahaman', eight)
    school.student_admission(rafsan)
    rupnika = Student('Rupnika Rahaman', eight)
    school.student_admission(rupnika)


    #add Subjects
    physics_teacher = Teacher('Nurul Absar')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Sumon sir')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    math_teacher = Teacher('Shukantho sir')
    math = Subject('math', math_teacher)
    eight.add_subject(math)
    
    eight.take_semester_final()


    print(school)
        


if __name__=='__main__':
    main()