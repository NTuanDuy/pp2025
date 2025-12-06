class Student:
    def __init__(self, student_id, name, bday):
        self.id = student_id
        self.name = name
        self.bday = bday
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, bday: {self.bday}"


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
    
    def __str__(self):
        return f"id: {self.id}, name: {self.name}"

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
            student = Student(student_id, name, bday)
            self.students.append(student)
    
    def enter_courses(self):
        numb = int(input("enter number of courses: "))
        for i in range(numb):
            course_id = input(f"enter id for course {i+1}: ")
            course_name = input(f"enter name for course {i+1}: ")
            course = Course(course_id, course_name)
            self.courses.append(course)
    
    def enter_marks(self):
        course_id = input("enter course id to input marks: ")
        course = self.find_course(course_id)
        
        if not course:
            print("invalid course / doesn't exist")
            return
        
        for student in self.students:
            mark_value = float(input(f"enter mark for {student.name} (id: {student.id}): "))
            mark = Mark(student, course, mark_value)
            self.marks.append(mark)
    
    def display_students_infos(self):
        print("\n all stored information in student list:")
        for student in self.students:
            print(student)
    
    def display_courses_infos(self):
        print("\n all stored information in course list:")
        for course in self.courses:
            print(course)
    
    def display_marks(self, course_id):

        course = self.find_course(course_id)
        
        if not course:
            print("course not found")
            return
        
        print(f"\n marks for course {course_id}:")
        for student in self.students:
            mark = self.find_mark(student, course)
            if mark:
                print(f"{student.name} [id: {student.id}] : {mark.score}")
            else:
                print(f"{student.name} [id: {student.id}] : no mark")
    
    def find_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                print("found matching course")
                return course
        return None
    
    def find_mark(self, student, course):
        for mark in self.marks:
            if mark.student.id == student.id and mark.course.id == course.id:
                print("found matching mark")
                return mark
        return None



if __name__ == "__main__":
    newsystemobject = ManagementSystem()  
    newsystemobject.enter_students()
    newsystemobject.enter_courses()
    newsystemobject.enter_marks()

    print("-- all student infos / course infos :--")
    newsystemobject.display_students_infos()
    newsystemobject.display_courses_infos()
    print("-- hello im a closing print --")
    course_id = input("\n enter course id to show marks of said course: ")
    newsystemobject.display_marks(course_id)