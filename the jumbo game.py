import random

def login():
    print("Welcome to Jambo Game!")
    name = input("Please enter your name: ")
    mobile = input("Please enter your mobile number: ")
    print(f"Hello, {name}! Let's start the game.\n")
    return name

def menu():
    print("Choose your difficulty level:")
    print("1. Easy (Bet: 100 - 1000)")
    print("2. Medium (Bet: 1000 - 50000)")
    print("3. Hard (Bet: 50000 - 100000)")
    level = int(input("Enter 1, 2, or 3: "))
    return level

def play_game(level, name):
    chances = 3
    guess_counter = 0
    amount = 0

    if level == 1:
        amount = int(input("Enter your bet amount (100 - 1000): "))
        multiplier = 10
    elif level == 2:
        amount = int(input("Enter your bet amount (1000 - 50000): "))
        multiplier = 20
    elif level == 3:
        amount = int(input("Enter your bet amount (50000 - 100000): "))
        multiplier = 50
    else:
        print("Invalid level selected!")
        return

    number_to_guess = random.randint(0, 5)
    print("\nYou have 3 chances to guess the number between 0 and 5.\n")

    while guess_counter < chances:
        guess_counter += 1
        my_guess = int(input(f"Attempt {guess_counter}: Enter your guess: "))

        if my_guess == number_to_guess:
            print(f"Congratulations, {name}! The number was {number_to_guess}.")
            print(f"You won! Your payout is {amount * multiplier}.\n")
            break

        elif my_guess > number_to_guess:
            print("Your guess is higher.")
        
        elif my_guess < number_to_guess:
            print("Your guess is lesser.")  

        if guess_counter == chances:
            print(f"Oops, sorry {name}. The number was {number_to_guess}. Better luck next time!\n")

# Main Program
user_name = login()
selected_level = menu()
play_game(selected_level, user_name)
