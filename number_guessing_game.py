import random
import time

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You will be given a number of chances to guess the correct number based on the difficulty level.")

def select_difficulty():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        elif choice == '3':
            return 3
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def get_number_to_guess():
    return random.randint(1, 100)

def play_game():
    chances = select_difficulty()
    number_to_guess = get_number_to_guess()
    attempts = 0
    start_time = time.time()

    print(f"\nGreat! You have selected the difficulty level with {chances} chances.")
    print("Let's start the game!")

    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Incorrect! The number is greater than", guess)
        elif guess > number_to_guess:
            print("Incorrect! The number is less than", guess)
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {elapsed_time:.2f} seconds.")
            return attempts

    print(f"Sorry, you've run out of chances. The correct number was {number_to_guess}.")
    return attempts

def main():
    high_scores = {'easy': float('inf'), 'medium': float('inf'), 'hard': float('inf')}

    while True:
        display_welcome_message()
        attempts = play_game()

        if attempts < high_scores['easy']:
            print("New high score for Easy difficulty!")
            high_scores['easy'] = attempts
        elif attempts < high_scores['medium']:
            print("New high score for Medium difficulty!")
            high_scores['medium'] = attempts
        elif attempts < high_scores['hard']:
            print("New high score for Hard difficulty!")
            high_scores['hard'] = attempts

        print("\nCurrent High Scores:")
        print(f"Easy: {high_scores['easy']} attempts")
        print(f"Medium: {high_scores['medium']} attempts")
        print(f"Hard: {high_scores['hard']} attempts")

        play_again = input("\nDo you want to play again? (yes or no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
