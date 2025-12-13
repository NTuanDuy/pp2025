import math
import numpy as numpymodule



class Student:
    def __init__(self, student_id, name, bday):
        self.id = student_id
        self.name = name
        self.bday = bday
        self.gpa = 0.0

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, bday: {self.bday} , gpa :{self.gpa}"


class Course:
    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credits = credit

    def __str__(self):
        return f"id: {self.id}, name: {self.name} , creditscore : {self.credits}"


class Mark:
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = score

    def __str__(self):
        return f"{self.student.name} | {self.course.name}: {self.score}"


class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def enter_students(self):
        numb = int(input("enter number of students: "))
        for i in range(numb):
            student_id = input(f"enter id of student {i+1}: ")
            name = input(f"enter name of student {i+1}: ")
            bday = input(f"enter birthday of student {i+1}: ")
            self.students.append(Student(student_id, name, bday))

    def enter_courses(self):
        numb = int(input("enter number of courses: "))
        for i in range(numb):
            course_id = input(f"enter id for course {i+1}: ")
            course_name = input(f"enter name for course {i+1}: ")
            credit = int(input(f"enter credit for course {i+1}: "))
            self.courses.append(Course(course_id, course_name, credit))

    def enter_marks(self):
        course_id = input("enter course id to input marks: ")
        course = self.find_course(course_id)
        if not course:
            return
        for student in self.students:
            mark_value = float(input(f"enter mark for {student.name} (id: {student.id}): "))
            floored_mark = math.floor(mark_value * 10) / 10
            self.marks.append(Mark(student, course, floored_mark))

    def display_students_infos(self):
        print("||Student_Infos Display||")
        for student in self.students:
            print(student)

    def display_courses_infos(self):
        print("||Courses Display||")
        for course in self.courses:
            print(course)

    def display_marks(self, course_id):
        print("||Marks Display||")
        course = self.find_course(course_id)
        if not course:
            return
        for student in self.students:
            mark = self.find_mark(student, course)
            if mark:
                print(f"{student.name} [id: {student.id}] : {mark.score}")
            else:
                print(f"{student.name} [id: {student.id}] : no mark")

    def find_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def find_mark(self, student, course):
        for mark in self.marks:
            if mark.student.id == student.id and mark.course.id == course.id:
                return mark
        return None

    def calc_gpa(self, student):
        score_table = []
        weight_table = []
        for mark_child in self.marks:
            if mark_child.student.id == student.id:
                score_table.append(mark_child.score)
                weight_table.append(mark_child.course.credits)
        if not score_table:
            student.gpa = 0
            return 0
        score_table = numpymodule.array(score_table)
        weight_table = numpymodule.array(weight_table)
        gpa_holder = numpymodule.sum(score_table * weight_table) / numpymodule.sum(weight_table)
        student.gpa = round(gpa_holder, 2)
        return student.gpa

    def update_gpa_list(self):
        for student in self.students:
            self.calc_gpa(student)

    def yield_gpa(self, student):
        return student.gpa

    def sort_students_via_gpa(self):
        self.update_gpa_list()
        self.students.sort(key=self.yield_gpa, reverse=True) # ADS sort algo sucks !!!!

    def display_sorted_students(self):
        print("List Of Students | GPA SORTED.")
        self.sort_students_via_gpa()
        for student in self.students:
            print(student)
       


if __name__ == "__main__":
    newsystemobject = ManagementSystem()
    newsystemobject.enter_students()
    newsystemobject.enter_courses()
    newsystemobject.enter_marks()
    newsystemobject.display_students_infos()
    newsystemobject.display_courses_infos()
    newsystemobject.display_sorted_students()
    course_id = input("enter course id to show marks of course: ")
    newsystemobject.display_marks(course_id)


