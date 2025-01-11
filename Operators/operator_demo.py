
"""
A+ : 81 - 100
A : 71 - 80
A- : 61 - 70
B : 51 - 60
C : 40 - 50
"""
pass_marks = 40
student_marks = int(input("Enter Marks: "))

if student_marks >= pass_marks :
    if student_marks > 100:
        print("Invalid Marks!!!!")
    else:
        print("Successfully Passed the Exam.")

    if 40 < student_marks <= 50:
        print("Grade C")
    elif 50 < student_marks <= 60:
        print("Grade B")
    elif 60 < student_marks <= 70:
        print("Grade A-")
    elif 70 < student_marks <= 79:
        print("Grade A")
    elif 80 <= student_marks <= 100:
        print("Grade A+")

else:
    print("Failed to the Exam.Grade F")