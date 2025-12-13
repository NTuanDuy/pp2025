class Course:
    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credits = credit

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, credits: {self.credits}"
