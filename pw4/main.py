from domains.management import ManagementSystem
import input
import output

def main():
    system = ManagementSystem()
    input.input_students(system)
    input.input_courses(system)
    input.input_marks(system)
    output.display_students(system)
    output.display_courses(system)
    output.display_sorted_students(system)

if __name__ == "__main__":
    main()
