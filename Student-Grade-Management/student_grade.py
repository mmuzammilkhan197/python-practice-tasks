name = input("Enter student's name: ")
m1 = int(input("Enter marks in Subject 1 (out of 100): "))
m2 = int(input("Enter marks in Subject 2 (out of 100): "))
m3 = int(input("Enter marks in Subject 3 (out of 100): "))

if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100):
    print("Invalid Marks")
else:
    total = m1 + m2 + m3
    percentage = total / 300 * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("\n" + "=" * 35)
    print("         STUDENT RESULT")
    print("=" * 35)
    print(f"Name         : {name}")
    print(f"Total Marks  : {total} / 300")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")
    print("=" * 35)