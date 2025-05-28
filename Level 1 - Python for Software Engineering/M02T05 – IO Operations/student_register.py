
student_s = []
student_number = []

student_count = int(input(f"Please give the number of students that will write exam: "))


with open('C:\\Users\\WernerV\\Documents\\GitHub\\WV25050018135\\Level 1 - Python for Software Engineering\\M02T05 – IO Operations\\reg_form.py', 'a+', encoding="utf-8") as student_s:
    for lines in range(student_count):
        student_number = str(input(f"Please enter student's number for attendance register: "))
        student_s.write(student_number + ":    _________" + "\n")
print(f" the amount of student numbers input is {student_count}")
print(student_s)