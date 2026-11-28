student = {
    "name": "Muzammil",
    "age": 19,
    "field": "BCIS",
    "marks": 85
}

def show_student():
    print("Name  :", student["name"])
    print("Age   :", student["age"])
    print("Field :", student["field"])
    print("Marks :", student["marks"])

def check_even(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

print("===== Student Information =====")
show_student()

student["marks"] = 96
print("\n===== After Updating Marks =====")
show_student()

if student["marks"] >= 50:
    print("\nResult: Pass")
else:
    print("\nResult: Fail")

print("\n===== Keys and Values =====")
for key, value in student.items():
    print(key, ":", value)

subjects = ["Python", "ICT", "English", "Math", "Programming"]

print("\n===== Subjects =====")
for subject in subjects:
    print(subject)

print("\n===== Numbers 1 to 5 =====")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\n===== Even or Odd =====")
check_even(80)
check_even(77)

marks = [80, 75, 90, 65, 85]

print("\n===== Marks Calculation =====")
print("Total marks  :", sum(marks))
print("Maximum marks:", max(marks))
print("Minimum marks:", min(marks))