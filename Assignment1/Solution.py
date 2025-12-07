# Part1
class Student:
    def __init__(self, name, student_id, courses_and_grades):
        self.name = name
        self.student_id = student_id
        self.courses_and_grades = courses_and_grades
def get_average_grade(self):
        total = sum(self.courses_and_grades.values())
        count = len(self.courses_and_grades)
        return total / count 
def add_courses_and_grades(self, course_name, grade):
        self.courses_and_grades[course_name] = grade
def get_honors_courses(self, threshold=90):
    honors = []
    for course, grade in self.courses_and_grades.items():
        if grade >= threshold:
            honors.append(course)
    return honors
def get_unique_grades(self):
    return set(self.courses_and_grades.values())

# Part2
all_students = []
s1 = Student(name="Alice", student_id=1, courses_and_grades={"Math": 95, "English": 88, "Science": 92})
s2 = Student(name="Bob", student_id=2, courses_and_grades={"Math": 78, "English": 85, "History": 80})
s3 = Student(name="Charlie", student_id=3, courses_and_grades={"Math": 90, "Science": 93, "Art": 87})
all_students.extend([s1, s2, s3])
for student in all_students:
    print(student.name, student.student_id, student.courses_and_grades)

for student in all_students:
    avg = student.get_average_grade()
    if avg > 80:
        honors_courses = student.get_honors_courses()
        print(f"{student.name} has an excellent average grade of {avg:.2f}"
              f" and the following honors courses: {"honors_courses"}")
    else:
        student.add_courses_and_grades("Study Skills", 100)
        print(f"Added 'Study Skills' with grade 100 for {student.name}.")