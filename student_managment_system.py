class Student:
    def __init__(self, first_name: str, last_name: str, studnet_id: int, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = studnet_id
        self.age = age


class StudentManagement:
    students_database = {}

    def accept(self, student: Student):
        #print(student.first_name)
        if student.student_id in self.students_database:
            print(f"Student with id {student.student_id} already exists.")
        else:
            self.students_database[student.student_id] = [student.first_name, student.last_name, student.age]
            #print(self.students_database[1][2])

    def search(self):
        print(" ¯\_(ツ)_/¯ ")
        ## Dont know how to do this method and how to implement it.
        
        
    def display(self, student_id: int):
        if student_id in self.students_database:
            print(f"{self.students_database[student_id][0]} {self.students_database[student_id][1]} is {self.students_database[student_id][2]}-years old and has an id of {student_id}.")
        else:
            print(f"Student with id {student_id} does not exist.")

    def delete(self, student_id: int):
        if student_id in self.students_database:
            self.students_database.pop(student_id)
            print(f"Student with id {student_id} removed.")
        else:
            print(f"Student with id {student_id} does not exist.")



if __name__ == "__main__":

    student1 = Student("John", "Doe", 1, 18)
    student2 = Student("Peter", "Oswell", 1, 15)
    student3 = Student("Lilliam", "Pumpernickle", 2, 22)
    student_management = StudentManagement()
    student_management.accept(student1)
    student_management.accept(student2)
    student_management.accept(student3)
    student_management.display(3)
    student_management.display(2)
    student_management.delete(1)
    student_management.display(1)