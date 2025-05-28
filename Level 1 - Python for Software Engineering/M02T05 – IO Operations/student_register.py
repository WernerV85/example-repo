#path = "C:\\Users\\WernerV\\Documents\\GitHub\\WV25050018135\\Level 1 - Python for Software Engineering\\M02T05 – IO Operations\\reg_form.py"
student_s = ""

student_count = int(input(f"Please give the number of students that will write exam: "))

for line in student_count:
    student_number = input(f"Please enter student's number for attendance register: ")
    lines.append(line)
print(lines)

with open("C:\\Users\\WernerV\\Documents\\GitHub\\WV25050018135\\Level 1 - Python for Software Engineering\\M02T05 – IO Operations\\reg_form.py" , "a+") as file:
    for line in file:
        for lines in student_count:
            student_number = input(f"Please enter student's number for attendance register: ")
            lines.append(line)
            file.write(student_number + "____________" + "\n")
        print(lines)
