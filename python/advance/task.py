# wap to store student details in csv file using oops and file handling

import csv
create = open('studen.csv', 'w')
b = csv.writer(create)
b.writerow(['rollno', 'name', 'age', 'degree', 'course'])
create.close()
class Student:
    def __init__(self,rollno,name, age, degree, course):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.degree = degree
        self.course = course
    
    # def create(self):
    #     file = open('student.csv', 'w')
    #     file_w = csv.writer(file)
    #     file_w.writerow(['rollno', 'name', 'age', 'degree', 'course'])

    def store(self):
        file = open('student.csv', 'a')
        file_w = csv.writer(file)
        file_w.writerow([self.rollno, self.name, self.age, self.degree, self.course])
        file.close()

obj = Student(183034, 'Anand', 22, 'B.E', 'ECE')
# obj.create()
obj.store()
obj2 = Student(194108,'Omen', 21, "B.E", 'CSE')
obj2.store()