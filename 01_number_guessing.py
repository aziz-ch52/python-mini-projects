import random

def number_guessing_game():
    print("\n================================")
    print("       NUMBER GUESSING GAME")
    print("================================")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 7

    print("\nI have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            # Validate the guessing range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            # Check the user's guess
            if guess == secret_number:
                print("\nCongratulations! You guessed correctly!")
                print(f"Secret Number: {secret_number}")
                print(f"Attempts Used: {attempts}")
                break

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            print(f"Attempts Remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    else:
        print("\nGame Over! You have used all your attempts.")
        print(f"The correct number was: {secret_number}")

    print("\n================================")


# Main program
while True:

    number_guessing_game()

    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()

    if play_again not in ("yes", "y"):
        print("\nThanks for playing! Goodbye.")
        break
