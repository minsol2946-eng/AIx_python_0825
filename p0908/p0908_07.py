from project import students
from project import student


stus=students.Students()
print(len(stus.slist))

s1=student.student(1,"김민솔",100,100,100)
print(s1)
stus.add(student.student(2,"멍멍이",100,100,100))

stus.print()