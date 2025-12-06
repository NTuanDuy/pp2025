students = []
courses = []
marks = {}


def input_student_numb():
    numb = int(input("enter student numbers :"))
    return numb

def input_info_student(numb):
    for i in range(numb):
        student_id = input(f"enter id of student{i+1}: ")
        name = input(f"enter name {i+1}: ")
        bday = input(f"enter bday {i+1}: ")
        students.append({"id": student_id, "name": name, "bday": bday})

def input_course_number():
    numb2 = int(input("enter number of courses: "))
    return numb2

def input_info_course(numb2):
    for i in range(numb2):
        course_id = input(f"enter id for course {i+1}: ")
        course_name = input(f"enter name {i+1}: ")
        courses.append({"id": course_id, "name": course_name})

def input_course_marks():
    course_id = input("enter course id to input marks ")
    if course_id not in [c["id"] for c in courses]:
        print("invalid course / doesnt exist")
        return
    marks[course_id] = {}
    for student in students:
        mark = float(input(f"enter mark for {student['name']} (id: {student['id']}): "))
        marks[course_id][student["id"]] = mark


def list_courses():
    print("\ncourse informations")
    for course in courses:
        print(f"id: {course['id']}, Name: {course['name']}")

def list_students():
    print("\nstudent informations")
    for student in students:
        print(f"id: {student['id']}, Name: {student['name']}, Bday: {student['bday']}")

def show_marks(course_id):
    if course_id not in marks:
        print("no marks found within this course id")
        return
    print(f"\nmarks for course {course_id}")
    for student in students:
        studentids = student["id"]
        if studentids in marks[course_id]:
            print(f"{student['name']} (id: {studentids}) >> {marks[course_id][studentids]}")
        else:
            print(f"{student['name']} (id: {studentids}) >> no mark")
            
