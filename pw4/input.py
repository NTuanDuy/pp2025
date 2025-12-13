from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import math

def input_students(system):
    n = int(input("enter number of students: "))
    for _ in range(n):
        sid = input("id: ")
        name = input("name: ")
        bday = input("birthday: ")
        system.add_student(Student(sid, name, bday))

def input_courses(system):
    n = int(input("enter number of courses: "))
    for _ in range(n):
        cid = input("id: ")
        name = input("name: ")
        credit = int(input("credit: "))
        system.add_course(Course(cid, name, credit))

def input_marks(system):
    cid = input("enter course id: ")
    course = system.find_course(cid)
    if not course:
        return
    for s in system.students:
        raw = float(input(f"mark for {s.name}: "))
        score = math.floor(raw * 10) / 10
        system.add_mark(Mark(s, course, score))
