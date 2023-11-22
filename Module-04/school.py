class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f"Student With name: {self.name}, class: {self.current_class}, id: {self.id}"


class Teacher:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f"Teacher With name: {self.name}, class: {self.current_class}, id: {self.id}"


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee > 6500:
            return "not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name, "C", id)
            self.students.append(student)
            return f"{name} is enrolled with id: {id}, extra money : {fee-6500}"

    def __repr__(self) -> str:
        print("welcome to", self.name)
        print("Our Teachers")
        for teacher in self.teachers:
            print(teacher)
        print("Our Student")
        for student in self.students:
            print(student)
        return "all done for now"


# Simran = Student("Simran Rahaman", 10, 31)
# Rafsan = Student("Rafsan Rahaman", "Algorithm", 44)
# print(Simran)
# print(Rafsan)

phitron = School("Phitron")
phitron.enroll("Alia", 5200)
phitron.enroll("Ranbir", 8000)
phitron.enroll("JKR", 6500)

phitron.add_teacher("John", "DS")
phitron.add_teacher("Jerry", "C++")
phitron.add_teacher("Tom", "Algorithm")
print(phitron)
