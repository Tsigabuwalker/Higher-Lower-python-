import random

def higher_lower_game():
    print("Welcome to the Higher-Lower Game!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue
            
            if guess < secret_number:
                print("Higher! Try again.")
            elif guess > secret_number:
                print("Lower! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        higher_lower_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    higher_lower_game()