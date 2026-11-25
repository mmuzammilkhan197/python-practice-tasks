
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

print("=" * 40)
print("       ROCK PAPER SCISSORS GAME")
print("=" * 40)

while user_score < 5 and computer_score < 5:

    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = input("\nEnter your choice: ")

    match user_choice:
        case "1":
            user = "Rock"
        case "2":
            user = "Paper"
        case "3":
            user = "Scissors"
        case "4":
            print("Game Exited!")
            break
        case _:
            print("Invalid Choice! Try Again.")
            continue

    computer = random.choice(choices)

    print("\nYou selected:", user)
    print("Computer selected:", computer)

    match (user, computer):
        case (a, b) if a == b:
            print("Result: Draw!")

        case ("Rock", "Scissors") | ("Paper", "Rock") | ("Scissors", "Paper"):
            print("Result: You Win!")
            user_score += 1

        case _:
            print("Result: Computer Wins!")
            computer_score += 1

    print("\nYour Score:", user_score)
    print("Computer Score:", computer_score)

print("\n" + "=" * 40)

if user_score == 5:
    print("Congratulations! You Won the Game!")

elif computer_score == 5:
    print("Computer Won the Game!")

print("Final Score:")
print("You:", user_score)
print("Computer:", computer_score)

print("=" * 40)
