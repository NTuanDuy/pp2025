class Student:
    def __init__(self, student_id, name, bday):
        self.id = student_id
        self.name = name
        self.bday = bday
        self.gpa = 0.0

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, bday: {self.bday}, gpa: {self.gpa}"
