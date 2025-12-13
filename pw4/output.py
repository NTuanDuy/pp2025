def display_students(system):
    for s in system.students:
        print(s)

def display_courses(system):
    for c in system.courses:
        print(c)

def display_sorted_students(system):
    system.sort_students_by_gpa()
    print("STUDENTS SORTED BY GPA")
    for s in system.students:
        print(s)
