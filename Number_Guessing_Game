import random

print("Welcome to the Number Guessing Game!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def number_guessing_game():
    answer = random.randint(1, 20)

    if difficulty == 'easy':
        attempts = 10
        print("Easy it is! You have 10 attempts.")
    elif difficulty == 'hard':
        attempts = 5
        print("You made your bed! You have 5 attempts.")
    else:
        print("Invalid difficulty. Defaulting to 'easy'.")
        attempts = 10
        print("Easy it is! You have 5 attempts.")

    while attempts > 0:
        try:
            user_guess = int(input("Guess a number between 1 and 20: ").strip())
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_guess == answer:
            print("Winner winner! Chicken dinner.")
            break  # Exit the loop if the user wins
        elif user_guess > answer:
            print("Guess lower.")
            attempts -= 1
        elif user_guess < answer:
            print("Guess higher.")
            attempts -= 1

        if attempts == 0:
            print(f"Sorry, you're out of attempts. The number was {answer}.")
        else:
            print(f"You have {attempts} attempts remaining.")


number_guessing_game()
