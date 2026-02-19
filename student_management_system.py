# COLOR CODES
RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"


class GradeSystem:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade_value):
        self.grades.append(grade_value)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def letter_grade(self):
        avg = self.calculate_average()

        if avg >= 90: return "AA"
        elif avg >= 85: return "BA"
        elif avg >= 80: return "BB"
        elif avg >= 75: return "CB"
        elif avg >= 70: return "CC"
        elif avg >= 65: return "DC"
        elif avg >= 60: return "DD"
        elif avg >= 50: return "FD"
        else: return "FF"

    def show_status(self):
        return "Passed" if self.calculate_average() >= 50 else "Failed"


class GraduateStudent(GradeSystem):
    def __init__(self, student_name, student_id, thesis_grade):
        super().__init__(student_name, student_id)
        self.thesis_grade = thesis_grade

    def calculate_average(self):
        course_avg = super().calculate_average()
        return (course_avg + self.thesis_grade) / 2


# List to store students
students = []

student1 = GradeSystem("Ali", 101)
student1.add_grade(70)
student1.add_grade(80)

student2 = GradeSystem("Zeynep", 102)
student2.add_grade(90)
student2.add_grade(95)

grad_student = GraduateStudent("Ayse", 201, 85)
grad_student.add_grade(60)
grad_student.add_grade(80)

students.extend([student1, student2, grad_student])


# Color formatting functions
def colored_letter(letter):
    if letter in ["AA", "BA", "BB"]:
        return GREEN + letter + RESET
    elif letter in ["CB", "CC", "DC"]:
        return YELLOW + letter + RESET
    else:
        return RED + letter + RESET


def colored_status(status):
    return GREEN + status + RESET if status == "Passed" else RED + status + RESET


# Output
for student in students:
    avg = round(student.calculate_average(), 2)
    letter = student.letter_grade()
    status = student.show_status()

    print(BOLD + CYAN + "\n===== STUDENT INFORMATION =====" + RESET)
    print(MAGENTA + "Name: " + RESET + student.student_name)
    print(MAGENTA + "ID: " + RESET + str(student.student_id))
    print(MAGENTA + "Average: " + RESET + BOLD + str(avg) + RESET)
    print(MAGENTA + "Letter Grade: " + RESET + colored_letter(letter))
    print(MAGENTA + "Status: " + RESET + colored_status(status))
