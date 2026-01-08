from game_logic import play_game
from sessions_handler import load_sessions, save_sessions
from stats_handler import show_stats


def main():
    while True:
        print("\nWelcome to the Number Guessing Game!")
        print("What do you want to do today:")
        print("\n1. Guess a number")
        print("2. See my stats")
        print("3. Quit\n")

        sessions = load_sessions()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            session = play_game(sessions)
            sessions.append(session)
            save_sessions(sessions)
        elif choice == "2":
            show_stats(sessions)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try Again.")


if __name__ == "__main__":
    main()
