class Student:

    num_students = 0
    def __init__(self,name,age):
       self.name = name
       self.age = age
       Student.num_students+=1
    
student1 = Student("Alice", 22)
student2 = Student("Bob", 23)
student3 = Student("dina", 20)
student4 = Student("deva", 21)

print(f"there are {Student.num_students} students in the class named {student1.name} , {student2.name} , {student3.name} , {student4.name}.")