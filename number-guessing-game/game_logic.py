import time
from random import randint


def choose_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid difficulty. Try again.")


def play_game(sessions):
    difficulty = choose_difficulty()
    target_number = randint(1, 100)
    chances = 10 if difficulty == "easy" else 5 if difficulty == "medium" else 3

    print(f"Great! You have selected the {difficulty.capitalize()} difficulty level.")
    print("Let's start the game!")

    session = {
        "difficulty": difficulty,
        "target_number": target_number,
        "guesses": [],
        "attempts": 0,
        "won": False,
        "duration_seconds": 0,
    }

    start_time = time.time()

    while chances > session["attempts"]:
        try:
            guess = int(input("\nEnter your guess (1-100): "))

            if guess < 0 or guess > 100:
                raise ValueError

            session["attempts"] += 1

            session["guesses"].append(guess)

            if guess == target_number:
                session["won"] = True
                print(
                    f"Congratulations! You guessed the correct number in {session['attempts']} attempts."
                )
                break
            elif guess > target_number:
                print(f"Incorrect! The number is less than {guess}.")
            elif guess < target_number:
                print(f"Incorrect! The number is greater than {guess}.")
        except ValueError:
            print("Invalid guess. Try Again.")
    else:
        print(f"You ran out of chances. Target number was {target_number}.")

    end_time = time.time()
    duration_seconds = int(end_time - start_time)
    session["duration_seconds"] = duration_seconds
    return session
