# balance = 300000
# correct_pin = "1234"

# print("===== Welcome to Simple ATM =====\n")

# name = input("Enter your name: ")
# pin = input("Enter your PIN: ")

# if correct_pin == pin:

#     print(f"\nWelcome {name}!")

#     while True:

#         print("\n1. Check Balance")
#         print("2. Deposit Balance")
#         print("3. Withdraw Balance")
#         print("4. Exit")

#         choice = input("\nChoose an option (1-4): ")

#         match choice:

#             case "1":
#                 print(f"Your Current Balance: Rs. {balance}")

#             case "2":
#                 amount = int(input("Enter amount to deposit: "))

#                 if amount > 0:
#                     balance += amount
#                     print(f"New Balance: Rs. {balance}")
#                 else:
#                     print("Enter a valid amount!")

#             case "3":
#                 amount = int(input("Enter amount to withdraw: "))

#                 if amount > 0 and amount <= balance:
#                     balance -= amount
#                     print(f"New Balance: Rs. {balance}")
#                 else:
#                     print("Invalid amount!")

#             case "4":
#                 print(f"Thank you {name} for visiting this ATM Program!")
#                 break

#             case _:
#                 print("Invalid choice!")

# else:
#     print("Invalid PIN!")
def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even(3))
print(is_even(56))
