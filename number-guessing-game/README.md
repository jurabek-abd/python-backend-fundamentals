# Number Guessing Game CLI

A simple command-line interface (CLI) number guessing game where you try to guess a randomly generated number. Built with Python using only standard library modules.

**Project URL:** https://roadmap.sh/projects/number-guessing-game/solutions?u=692db4d2a17ff74763dc81f1

## Features

- ✅ Three difficulty levels (Easy, Medium, Hard)
- ✅ Random number generation between 1-100
- ✅ Smart hints after each guess (higher/lower)
- ✅ Game session tracking with JSON storage
- ✅ Comprehensive statistics dashboard
- ✅ Win rate and streak tracking
- ✅ Timer for each game session
- ✅ Input validation and error handling

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd number-guessing-game
```

2. The project is ready to use! No additional installation required.

## Project Structure

```
number-guessing-game/
├── game_logic.py           # Core game logic and difficulty selection
├── number_game.py          # Entry point and main menu
├── sessions_handler.py     # JSON file operations for game sessions
├── stats_handler.py        # Statistics calculation and display
├── sessions.json           # Game history storage (auto-created)
└── README.md
```

## Usage

Run the application using Python:

```bash
python number_game.py
```

### Main Menu Options

```
Welcome to the Number Guessing Game!
What do you want to do today:

1. Guess a number
2. See my stats
3. Quit
```

### Playing a Game

1. Select option `1` from the main menu
2. Choose your difficulty level:
   - **Easy**: 10 chances to guess
   - **Medium**: 5 chances to guess
   - **Hard**: 3 chances to guess
3. Enter your guesses (numbers between 1-100)
4. Receive hints after each guess
5. Win by guessing correctly or lose when you run out of chances

### Example Game Session

```bash
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess (1-100): 50
Incorrect! The number is less than 50.

Enter your guess (1-100): 25
Incorrect! The number is greater than 25.

Enter your guess (1-100): 35
Incorrect! The number is less than 35.

Enter your guess (1-100): 30
Congratulations! You guessed the correct number in 4 attempts.
```

### Viewing Statistics

Select option `2` from the main menu to view your performance stats:

```
My Stats:
Total games played: 15
Win rate: 73.3%
Average attempts in easy: 4.5
Average attempts in medium: 3.2
Average attempts in hard: N/A
Fastest win (seconds): 12
Current win streak: 3
```

Statistics include:
- **Total games played**: Count of all game sessions
- **Win rate**: Percentage of games won
- **Average attempts per difficulty**: Average guesses needed to win for each difficulty level
- **Fastest win**: Shortest time to win a game (in seconds)
- **Current win streak**: Number of consecutive wins

## Game Session Data

Each game session is stored with the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `difficulty` | String | Game difficulty (easy, medium, hard) |
| `target_number` | Integer | The number to guess (1-100) |
| `guesses` | List | All numbers guessed during the session |
| `attempts` | Integer | Total number of valid attempts made |
| `won` | Boolean | Whether the player won the game |
| `duration_seconds` | Integer | Time taken to complete the game |

## Data Storage

Game sessions are stored in `sessions.json` in the project directory. The file is automatically created on first use.

Example `sessions.json` structure:
```json
[
    {
        "difficulty": "medium",
        "target_number": 42,
        "guesses": [50, 25, 35, 40, 42],
        "attempts": 5,
        "won": true,
        "duration_seconds": 45
    },
    {
        "difficulty": "easy",
        "target_number": 73,
        "guesses": [50, 75, 70, 73],
        "attempts": 4,
        "won": true,
        "duration_seconds": 32
    }
]
```

## Error Handling

The application handles various scenarios gracefully:

- **Invalid input**: Validates that guesses are numbers between 1-100
- **Empty input**: Prompts user to enter a valid number
- **Invalid difficulty selection**: Asks user to try again with valid option
- **Corrupted JSON**: Recovers by starting with empty session list
- **Missing statistics**: Displays "None" or "N/A" for unplayed difficulty levels

## Development

### Code Organization

- **game_logic.py**: Handles difficulty selection and main game loop
- **sessions_handler.py**: Manages JSON file operations for persistent storage
- **stats_handler.py**: Calculates and displays player statistics
- **number_game.py**: Orchestrates the main menu and application flow

### Best Practices Implemented

- ✅ Modular code organization with separation of concerns
- ✅ Return values instead of printing from business logic
- ✅ Input validation with `.strip()` for whitespace handling
- ✅ Edge case handling (empty data, division by zero)
- ✅ Clear user feedback for all actions

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Number Guessing Game project](https://roadmap.sh/projects/number-guessing-game/solutions?u=692db4d2a17ff74763dc81f1).

---

**Project URL:** https://roadmap.sh/projects/number-guessing-game/solutions?u=692db4d2a17ff74763dc81f1
