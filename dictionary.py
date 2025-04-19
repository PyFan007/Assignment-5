student_marks = {'Alice': 85,'Bob': 90,'Charlie': 78,'Diana': 92,'Ethan': 88}
name = input("Enter the student's name: ")
marks = student_marks.get(name)
if marks is not None:
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found.")