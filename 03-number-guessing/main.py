"""
Number Guessing Game - Python Project 03
========================================
An interactive guessing game with difficulty levels, hints, and statistics.

🎯 LEARNING OBJECTIVES:
- Use the random module to generate random numbers
- Implement game logic with loops and conditionals
- Practice input validation
- Track and display game statistics
- Create difficulty levels
- Provide helpful hints to players

📚 CONCEPTS COVERED:
- Random number generation
- While loops and break statements
- If-elif-else conditionals
- Integer comparison
- Game state management
- User interaction
"""

import random

def display_welcome():
    """
    Display welcome message and game rules.
    
    LEARNING: Creating clear user interfaces with formatted output
    """
    print("\n" + "="*60)
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME!")
    print("="*60)
    print("\nHow to play:")
    print("1. I'll think of a number")
    print("2. You try to guess it")
    print("3. I'll give you hints (higher/lower)")
    print("4. Try to guess in as few attempts as possible!")
    print("="*60)

def choose_difficulty():
    """
    Let player choose difficulty level.
    
    Returns:
        tuple: (min_range, max_range, max_attempts)
    
    LEARNING: Functions can return multiple values as a tuple
    """
    print("\nChoose your difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    print("4. Expert (1-500, 5 attempts)")
    
    while True:
        choice = input("\nEnter difficulty (1-4): ").strip()
        
        if choice == '1':
            return 1, 50, 10  # min, max, attempts
        elif choice == '2':
            return 1, 100, 7
        elif choice == '3':
            return 1, 200, 5
        elif choice == '4':
            return 1, 500, 5
        else:
            print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")

def get_valid_guess(min_num, max_num):
    """
    Get a valid guess from the player.
    
    Args:
        min_num (int): Minimum valid number
        max_num (int): Maximum valid number
    
    Returns:
        int: Valid guess from player
    
    LEARNING: Input validation with error handling and range checking
    """
    while True:
        try:
            guess = int(input(f"\nEnter your guess ({min_num}-{max_num}): "))
            
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"❌ Please enter a number between {min_num} and {max_num}!")
        
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def give_hint(guess, target, min_num, max_num, attempts_left):
    """
    Provide hints to help the player.
    
    Args:
        guess (int): Player's guess
        target (int): The secret number
        min_num (int): Minimum range
        max_num (int): Maximum range
        attempts_left (int): Remaining attempts
    
    LEARNING: Complex conditional logic to provide appropriate feedback
    """
    difference = abs(guess - target)
    range_size = max_num - min_num
    
    # Distance-based hints
    if difference == 0:
        return  # They won!
    elif difference <= range_size * 0.05:  # Within 5% of range
        print("🔥 You're VERY HOT! So close!")
    elif difference <= range_size * 0.10:  # Within 10%
        print("🌡️ You're hot! Getting closer!")
    elif difference <= range_size * 0.20:  # Within 20%
        print("☀️ You're warm!")
    elif difference <= range_size * 0.40:  # Within 40%
        print("🌤️ You're lukewarm...")
    else:
        print("❄️ You're cold!")
    
    # Direction hint
    if guess < target:
        print("📈 The number is HIGHER")
    else:
        print("📉 The number is LOWER")
    
    # Urgency hint based on attempts left
    if attempts_left <= 2:
        print(f"⚠️ HURRY! Only {attempts_left} attempts left!")

def play_game():
    """
    Main game function.
    
    Returns:
        dict: Game statistics (won, attempts, etc.)
    
    LEARNING: 
    - Game loop implementation
    - State tracking with variables
    - Return dictionary for complex data
    """
    # Setup
    min_num, max_num, max_attempts = choose_difficulty()
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    won = False
    
    print(f"\n🎲 I'm thinking of a number between {min_num} and {max_num}")
    print(f"You have {max_attempts} attempts to guess it!")
    print("\nLet's begin! 🚀")
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        attempts_left = max_attempts - attempts + 1
        
        print(f"\n--- Attempt {attempts}/{max_attempts} ---")
        guess = get_valid_guess(min_num, max_num)
        
        if guess == secret_number:
            # WIN!
            print("\n" + "="*60)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print("="*60)
            print(f"✅ You guessed the number {secret_number} in {attempts} attempts!")
            won = True
            break
        else:
            # Provide hints
            give_hint(guess, secret_number, min_num, max_num, attempts_left)
    
    # Game over
    if not won:
        print("\n" + "="*60)
        print("💀 GAME OVER!")
        print("="*60)
        print(f"The secret number was: {secret_number}")
        print("Better luck next time! 🍀")
    
    return {
        'won': won,
        'attempts': attempts,
        'max_attempts': max_attempts,
        'number': secret_number,
        'range': (min_num, max_num)
    }

def display_statistics(games_history):
    """
    Display overall game statistics.
    
    Args:
        games_history (list): List of game result dictionaries
    
    LEARNING: Analyzing data from a list of dictionaries
    """
    if not games_history:
        return
    
    total_games = len(games_history)
    games_won = sum(1 for game in games_history if game['won'])
    win_rate = (games_won / total_games) * 100
    
    total_attempts = sum(game['attempts'] for game in games_history)
    avg_attempts = total_attempts / total_games
    
    print("\n" + "="*60)
    print("📊 YOUR STATISTICS")
    print("="*60)
    print(f"Total Games Played: {total_games}")
    print(f"Games Won: {games_won}")
    print(f"Games Lost: {total_games - games_won}")
    print(f"Win Rate: {win_rate:.1f}%")
    print(f"Average Attempts: {avg_attempts:.1f}")
    
    if games_won > 0:
        won_games = [g for g in games_history if g['won']]
        best_score = min(g['attempts'] for g in won_games)
        print(f"Best Score: {best_score} attempts")
    
    print("="*60)

def main():
    """
    Main program loop.
    
    LEARNING: Program structure with game sessions and statistics tracking
    """
    display_welcome()
    
    games_history = []  # Track all games played
    
    while True:
        # Play one game
        result = play_game()
        games_history.append(result)
        
        # Calculate score (if won)
        if result['won']:
            score = 100 - (result['attempts'] - 1) * 10
            score = max(score, 10)  # Minimum score of 10
            print(f"\n⭐ Your score: {score} points!")
        
        # Ask to play again
        print("\n" + "-"*60)
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        
        if play_again != 'y':
            # Show statistics before exiting
            display_statistics(games_history)
            print("\n👋 Thanks for playing! Come back soon!")
            break

# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    """
    LEARNING: This ensures the game runs only when executed directly,
    not when imported as a module.
    """
    main()

# ============================================================================
# PRACTICE EXERCISES:
# ============================================================================
# 1. Add a "custom range" option where player sets min/max
# 2. Implement a "hints cost points" system
# 3. Add a two-player mode (one player sets number, other guesses)
# 4. Create a "reverse mode" where computer guesses your number
# 5. Add a leaderboard saved to a file
# 6. Implement a "streak" bonus for consecutive wins
# 7. Add sound effects (using winsound or pygame)
# 8. Create a "tournament mode" with multiple rounds
# 9. Add time-based scoring (faster guesses = more points)
# 10. Implement achievements system (e.g., "Win 5 games in a row")
