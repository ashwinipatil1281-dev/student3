import sys
marks = list(map(float, sys.argv[1:]))

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

print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
