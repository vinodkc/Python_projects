"""
Rock Paper Scissors Game - Python Project 07
===========================================
Classic rock-paper-scissors game with score tracking and multiple rounds.

🎯 LEARNING OBJECTIVES:
- Implement game logic with conditional statements
- Use random.choice() for computer moves
- Track scores across multiple rounds
- Create game loops with exit conditions
- Handle user input validation

📚 CONCEPTS COVERED:
- Game logic and rules implementation
- Random selection from lists
- Score tracking with variables
- Win/loss/tie conditions
- Input validation and error handling
"""

import random

def get_computer_choice():
    """
    Computer randomly selects rock, paper, or scissors.
    
    LEARNING: Using random.choice() to select from a list
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    """
    Get and validate user's choice.
    
    LEARNING: Input validation with loops
    """
    print("\nChoose your move:")
    print("1. 🪨 Rock")
    print("2. 📄 Paper")
    print("3. ✂️  Scissors")
    
    while True:
        choice = input("\nEnter your choice (1-3 or rock/paper/scissors): ").lower().strip()
        
        # Handle numeric input
        if choice == '1' or choice == 'rock' or choice == 'r':
            return 'rock'
        elif choice == '2' or choice == 'paper' or choice == 'p':
            return 'paper'
        elif choice == '3' or choice == 'scissors' or choice == 's':
            return 'scissors'
        else:
            print("❌ Invalid choice! Try again.")

def determine_winner(user, computer):
    """
    Determine the winner of the round.
    
    Returns:
        str: 'user', 'computer', or 'tie'
    
    LEARNING: Implementing game rules with conditional logic
    """
    if user == computer:
        return 'tie'
    
    # User wins conditions
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return 'user'
    
    # Otherwise computer wins
    return 'computer'

def get_emoji(choice):
    """
    Get emoji representation of choice.
    
    LEARNING: Using dictionaries for mapping values
    """
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    return emojis.get(choice, '❓')

def display_round_result(user_choice, computer_choice, winner):
    """
    Display the results of a single round.
    
    LEARNING: Formatted output for better UX
    """
    print("\n" + "="*60)
    print("⚔️  ROUND RESULT")
    print("="*60)
    print(f"You chose:     {get_emoji(user_choice)} {user_choice.upper()}")
    print(f"Computer chose: {get_emoji(computer_choice)} {computer_choice.upper()}")
    print("-"*60)
    
    if winner == 'tie':
        print("🤝 It's a TIE!")
    elif winner == 'user':
        print("🎉 YOU WIN this round!")
    else:
        print("💻 COMPUTER WINS this round!")
    
    print("="*60)

def display_scores(user_score, computer_score, ties):
    """
    Display current scores.
    """
    print("\n📊 CURRENT SCORES:")
    print("-"*40)
    print(f"You:      {user_score} wins")
    print(f"Computer: {computer_score} wins")
    print(f"Ties:     {ties}")
    print("-"*40)
    total = user_score + computer_score + ties
    if total > 0:
        win_rate = (user_score / total) * 100
        print(f"Your win rate: {win_rate:.1f}%")

def play_best_of(rounds):
    """
    Play a best-of-N match.
    
    LEARNING: Loop control and round tracking
    """
    user_score = 0
    computer_score = 0
    ties = 0
    rounds_needed = (rounds // 2) + 1
    
    print(f"\n🎮 Best of {rounds} match!")
    print(f"First to win {rounds_needed} rounds wins the match!")
    
    for round_num in range(1, rounds + 1):
        print(f"\n{'='*60}")
        print(f"ROUND {round_num} of {rounds}")
        print('='*60)
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_round_result(user_choice, computer_choice, winner)
        
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        else:
            ties += 1
        
        display_scores(user_score, computer_score, ties)
        
        # Check if someone has won the match
        if user_score >= rounds_needed:
            print("\n🏆 YOU WON THE MATCH! CONGRATULATIONS! 🏆")
            break
        elif computer_score >= rounds_needed:
            print("\n💻 COMPUTER WON THE MATCH! Better luck next time!")
            break
        
        if round_num < rounds:
            cont = input("\nPress Enter to continue to next round...")

def main():
    """
    Main game loop.
    """
    print("\n" + "="*60)
    print("🪨 📄 ✂️  ROCK PAPER SCISSORS")
    print("="*60)
    print("\nGame Rules:")
    print("• Rock beats Scissors")
    print("• Scissors beats Paper")
    print("• Paper beats Rock")
    print("="*60)
    
    overall_user_wins = 0
    overall_computer_wins = 0
    overall_ties = 0
    
    while True:
        print("\nGame Modes:")
        print("1. Single Round")
        print("2. Best of 3")
        print("3. Best of 5")
        print("4. View Overall Stats")
        print("5. Exit")
        
        mode = input("\nChoose mode (1-5): ").strip()
        
        if mode == '1':
            # Single round
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            winner = determine_winner(user_choice, computer_choice)
            
            display_round_result(user_choice, computer_choice, winner)
            
            if winner == 'user':
                overall_user_wins += 1
            elif winner == 'computer':
                overall_computer_wins += 1
            else:
                overall_ties += 1
        
        elif mode == '2':
            play_best_of(3)
        
        elif mode == '3':
            play_best_of(5)
        
        elif mode == '4':
            # Stats
            print("\n" + "="*60)
            print("📊 OVERALL STATISTICS")
            print("="*60)
            print(f"Your wins:     {overall_user_wins}")
            print(f"Computer wins: {overall_computer_wins}")
            print(f"Ties:          {overall_ties}")
            total = overall_user_wins + overall_computer_wins + overall_ties
            if total > 0:
                print(f"\nTotal games:   {total}")
                print(f"Win rate:      {(overall_user_wins/total)*100:.1f}%")
            print("="*60)
        
        elif mode == '5':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()

