import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7
guess = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100")
print("You have only 7 attempts.\n")

while guess != secret and attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess > secret:
        print("Too High! Try Again.\n")
    elif guess < secret:
        print("Too Low! Try Again.\n")
    else:
        print("Correct Guess! You Won!\n")

print("=" * 35)
print(f"Total Attempts: {attempts}")

if guess == secret:
    print("Result: You Won!")
else:
    print("Result: Game Over!")
    print(f"Secret Number was: {secret}")

print("=" * 35)
