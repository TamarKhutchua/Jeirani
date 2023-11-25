import random

def get_user_choice():
    while True:
        user_choice = input("Enter 'scissors', 'stone', or 'paper': ").lower()
        if user_choice in ['scissors', 'stone', 'paper']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'scissors', 'stone', or 'paper'.")

def get_computer_choice():
    return random.choice(['scissors', 'stone', 'paper'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'stone' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'stone')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    for _ in range(5):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print(f"User: {user_score} vs. Computer: {computer_score}")

if __name__ == "__main__":
    print("Welcome to the Jeyran Game!")
    play_game()

