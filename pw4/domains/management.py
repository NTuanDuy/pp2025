import math
import numpy as np
from .student import Student
from .course import Course
from .mark import Mark

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_mark(self, mark):
        self.marks.append(mark)

    def find_course(self, course_id):
        for c in self.courses:
            if c.id == course_id:
                return c
        return None

    def calc_gpa(self, student):
        scores = []
        weights = []
        for m in self.marks:
            if m.student.id == student.id:
                scores.append(m.score)
                weights.append(m.course.credits)
        if not scores:
            student.gpa = 0
            return 0
        scores = np.array(scores)
        weights = np.array(weights)
        student.gpa = round(np.sum(scores * weights) / np.sum(weights), 2)
        return student.gpa

    def update_all_gpa(self):
        for s in self.students:
            self.calc_gpa(s)

    def sort_students_by_gpa(self):
        self.update_all_gpa()
        self.students.sort(key=lambda s: s.gpa, reverse=True)
