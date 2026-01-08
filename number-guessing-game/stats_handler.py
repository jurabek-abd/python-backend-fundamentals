def show_stats(sessions):
    # Total Games Played
    total_games = len(sessions)

    # Win Rate
    wins = sum(1 for session in sessions if session["won"])
    win_rate = (wins / total_games * 100) if total_games > 0 else 0

    # Average Attempts Per Difficulty
    easy_sessions = list(filter(lambda s: s["difficulty"] == "easy", sessions))
    average_attempts_easy = (
        round(
            sum(s["attempts"] for s in easy_sessions) / len(easy_sessions),
            1,
        )
        if not len(easy_sessions) == 0
        else None
    )
    medium_sessions = list(filter(lambda s: s["difficulty"] == "medium", sessions))
    average_attempts_medium = (
        round(
            sum(s["attempts"] for s in medium_sessions) / len(medium_sessions),
            1,
        )
        if not len(medium_sessions) == 0
        else None
    )
    hard_sessions = list(filter(lambda s: s["difficulty"] == "hard", sessions))
    average_attempts_hard = (
        round(
            sum(s["attempts"] for s in hard_sessions) / len(hard_sessions),
            1,
        )
        if not len(hard_sessions) == 0
        else None
    )

    # Fastest Win
    filtered_sessions_won = list(filter(lambda s: s["won"], sessions))
    fastest_win = (
        min(filtered_sessions_won, key=lambda s: s["duration_seconds"])[
            "duration_seconds"
        ]
        if not len(filtered_sessions_won) == 0
        else None
    )

    # Current Win Streak
    current_streak = 0

    for session in reversed(sessions):
        if session["won"]:
            current_streak += 1
        else:
            break

    print("\nMy Stats:")
    print("Total games played:", total_games)
    print(f"Win rate: {win_rate:.1f}%")
    print(
        "Average attempts in easy:",
        average_attempts_easy if average_attempts_easy is not None else "N/A",
    )
    print(
        "Average attempts in medium:",
        average_attempts_medium if average_attempts_medium is not None else "N/A",
    )
    print(
        "Average attempts in hard:",
        average_attempts_hard if average_attempts_hard is not None else "N/A",
    )
    print(
        "Fastest win (seconds):",
        fastest_win if fastest_win is not None else "No wins yet",
    )
    print("Current win streak:", current_streak)
