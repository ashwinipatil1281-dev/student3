import sys

default_marks = [85, 90, 78, 88, 92]

if len(sys.argv) == 6:   # 5 marks + script name
    marks = list(map(float, sys.argv[1:]))
    source = "User Input"
else:
    marks = default_marks
    source = "Self-assigned"

if len(marks) != 5:
    print("Error: Please provide exactly 5 marks.")
    sys.exit(1)

average = sum(marks) / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print(f"Marks: {marks} ({source})")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
